
from FIXTURE.fixture_application import Application
from FIXTURE.db import DbFixture
import jsonpickle
import importlib
import pytest
import os.path
import json

#import importlib
#import jsonpickle

AppFixture = None  # Глобальная переменная - экземпляр фикстуры для запуска тестов
Parameters = None  # Глобальная переменная - экземпляр для хранения параметров считанных из конфиг файла "config.json"

#########################################################################################################################################################################################
#   Фикстура для подготовки к старту тестов:
#########################################################################################################################################################################################

@pytest.fixture
def app(request):

    #  1. Говорим что будем использовать глобальную переменную объявленную выше:
    global AppFixture

    # 2. Загружаем конфиг файл из корня проекта и читаем параметры секции web:
    web_config = load_config(request.config.getoption("--config"))['web']

    # 3. Если фикстура еще не существует или стала попорченой:
    if (AppFixture is None) or not AppFixture.is_valid():

        AppFixture = Application(browser =  web_config['browser'], base_url =  web_config['baseUrl'])

    # 4. Выполняем логин и создание сессии:
    AppFixture.session.Ensure_Login(username=web_config['username'], password=web_config['password'])

    # Чуть позже заменим логин на этот:
    #AppFixture.session.Ensure_Login_process(username =  web_config['username'], password =  web_config['password'])

    return AppFixture


##########################################################################################################################################################################################
#   Фикстура для подготовки к завершению тестов:
##########################################################################################################################################################################################

@pytest.fixture( scope="session", autouse = True )
def setup_finalizer(request):

    ####################################################################################################################
    # Функция завершающая работу после выполнения тестов
    ####################################################################################################################
    def finalisation():

        # 1. Выполняем логаут:
        AppFixture.session.Ensure_logout()  # Позже заменим на Ensure_Login c проверкой того, что мы еще залогинены:

        # 2. Выполняем уничтожение экземпляра фикстуры:
        AppFixture.Destroy()

    ####################################################################################################################

    # 1. Указываем что нужно вызвать при завершениии тестов.
    request.addfinalizer(finalisation)

    # 2. Возвращаем наверх экземпляр
    return AppFixture


##########################################################################################################################################################################################
#   Функция для загрузки параметров из конфигурационного файла
##########################################################################################################################################################################################

def load_config(file):

    # 1. Говорим что будем использовать глобальную переменную объявленную выше:
    global Parameters

    # 2. Если первый запуск и параметры еще не прочитали из конфиг файла, то надо прочитать:
    if Parameters is None:

        # 2.1 Формируем имя файла и путь для открытия файла с параметрами конфигурации:
        cfg_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)                     # Путь + Имя файла

        # 2.1 Открываем файл и читаем все в переменную Parameters (закрывать не надо так как with все сам сделает!)
        with open(cfg_file) as config_file:
            Parameters = json.load(config_file)

    # 3. Возвращаем наверх считанные параметры
    return Parameters

##########################################################################################################################################################################################
#   Указываем параметр для конфигурации в файле: to register custom command-line arguments and configuration options.
##########################################################################################################################################################################################

def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.json" )

##########################################################################################################################################################################################
# Добавляем функции для обработки динамической параметризации через METAFUNC pytest_generate_tests(metafunc)
##########################################################################################################################################################################################
#
# metafunc в Python — это объект, используемый в фреймворке pytest внутри хук-функции pytest_generate_tests для динамической параметризации тестов.
# Он позволяет генерировать тестовые случаи «на лету», анализировать аргументы функций и создавать вариации тестов без использования
# декоратора @pytest.mark.parametrize для каждого случая.

def pytest_generate_tests(metafunc):

    for AppFixture in metafunc.fixturenames:

        if AppFixture.startswith("dataadd_"): # Если данные для теста ADD берем из модуля...

            test_data = load_from_module(AppFixture)

            metafunc.parametrize(AppFixture, test_data, ids=[str(x) for x in test_data])

        elif AppFixture.startswith("datamod_"):  # Если данные для теста MOD берем из модуля...

            test_data = load_from_module(AppFixture)

            metafunc.parametrize(AppFixture, test_data, ids=[str(x) for x in test_data])


        elif AppFixture.startswith("json_"):

            test_data = load_from_json_file(AppFixture[5:])

            metafunc.parametrize(AppFixture,test_data, ids=[str(x) for x in test_data])


def load_from_module (module):

    if module == "dataadd_data_inventory":

        str_name = "DATA.%s" % module[8:]

        x = importlib.import_module(str_name).test_data_add  # Или можно взять constant из файла DATA\data_inventory.py

    elif module == "datamod_data_inventory":

        str_name = "DATA.%s" % module[8:]
  
        x = importlib.import_module(str_name).test_data_mod # Или можно взять constant из файла DATA\data_inventory.py
    
    return x


def load_from_json_file (file):

    with open( os.path.join(os.path.dirname(os.path.abspath(__file__)),"DATA/%s.json" % file)) as f:

        return jsonpickle.decode(f.read())

##########################################################################################################################################################################################
#   Фикстура для работы с базой данных
##########################################################################################################################################################################################

@pytest.fixture
def db(request):

    db_config = load_config(request.config.getoption("--config"))['db']

    dbFixture = DbFixture(host = db_config['host'],
                          name = db_config['name'],
                          user = db_config['user'],
                          password = db_config['password'])

    def fin():
        dbFixture.destroy()

    request.addfinalizer(fin)
    return dbFixture
