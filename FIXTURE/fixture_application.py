from FIXTURE.session_helper import SessionHelper
from FIXTURE.inventory_helper import InventoryHelper
from selenium  import webdriver


# Класс описывающий основую фикстуру для запуска тестов и осуществления логина и логаута
class Application:

    ####################################################################################################################
    # Контруктор класса
    ####################################################################################################################

    def __init__(self, browser, base_url):

        # 0. Сохраняем ссылку на страницу testlink
        self.base_url = base_url

        # 1. Проверяем какой браузер нужно стартовать - он прописан в конфиг файле "config.json"
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "ie":
            self.driver = webdriver.Ie()
        elif browser == "edge":
            self.driver = webdriver.Edge()
        else:
            raise ValueError("Unrecognised browser %s" % browser) # Ошибку перехватит Pytest

        # 2. Устанавливаем таймауты на ожидание: Для учебного приложения это не нужно все элементы сразу на странице
        self.driver.implicitly_wait(5)

        # 3. Создаем сессию и логинимся:
        self.session = SessionHelper(self)

        #4. Создаем помощника для работы с Inventory
        self.inventory = InventoryHelper(self)

        self.base_url = base_url

    ####################################################################################################################
    # Функция проверки того, что фикстура "не протухла"
    ####################################################################################################################

    def is_valid(self):

        try:
            self.driver.current_url
            return True
        except:
            return False

    ####################################################################################################################
    # Функция уничтожения сессии
    ####################################################################################################################

    def Destroy(self):

        # 1. Выходим из драйвера Selenium с очисткой всех ресурсов
        self.driver.quit()

