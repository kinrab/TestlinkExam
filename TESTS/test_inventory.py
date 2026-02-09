
from DATA.data_inventory import *
from random import randrange
import allure
import pytest

########################################################################################################################################################################
# Тест проверяющий создание нового инвентаря (тестовых стендов)
########################################################################################################################################################################

# Вариант параметризации через Pytest Mark Parameters:
@pytest.mark.parametrize("inventory_item", constant_data, ids =[repr(x) for x in constant_data ])
def test_add_inventory(app, inventory_item ):

    # 1. Открыть основное окно - так как оно может быть не открыто после другого теста.
    with allure.step(f'Open main window'):
        app.inventory.Open_main_window()

    # 2. Нажать на пункт меню Inventory и открыть на экране зону работы с инвентарем.
    with allure.step(f'Open inventory window'):
        app.inventory.Open_Inventory_window()

    # 3. Получим текущий список элементов:
    with allure.step(f'Get old list of inventory'):
        old_list = app.inventory.Get_inventory_list()

    # 4. Добавить новый элемент инвенторя (заполнить поля) и сохранить.
    with allure.step(f'Add new inventory item: Host={inventory_item.Inventory_Hostname} IPAddress={ inventory_item.Inventory_IPaddress} Owner={inventory_item.Inventory_Owner} Purpose={inventory_item.Inventory_Purpose} HW={inventory_item.Inventory_Hardware} Notes={inventory_item.Inventory_Notes}'):
        NewInventory = Inventory(Inventory_Hostname  = inventory_item.Inventory_Hostname,
                                 Inventory_IPaddress = inventory_item.Inventory_IPaddress,
                                 Inventory_Owner     = inventory_item.Inventory_Owner,
                                 Inventory_Purpose   = inventory_item.Inventory_Purpose,
                                 Inventory_Hardware  = inventory_item.Inventory_Hardware,
                                 Inventory_Notes     = inventory_item.Inventory_Notes)
        app.inventory.Add_new_inventory(NewInventory)

    # 5. Получим новый список элементов:
    with allure.step(f'Get new list of inventory'):
        new_list = app.inventory.Get_inventory_list()

    # 6. Добавим новый элемент в старый список чтобы списки стали равны:
    with allure.step(f'Add new inventory into old list'):
        old_list.append(NewInventory)

    # 7. Сравниваем списки применяя сортировку:
    with allure.step(f'Check Assert - lists comparation'):
        assert sorted(old_list) == sorted(new_list)

    # 8. Вернутся на главную страницу
    with allure.step(f'Return to main window'):
        app.inventory.Open_main_window()

########################################################################################################################################################################
# Тест проверяющий создание нового инвентаря (тестовых стендов)
########################################################################################################################################################################
# Вариант динамической параметризации pytest_generate_tests(metafunc)
# Имя параметра data_inventory_data формируется по правилам:
#   'data_' префикс для обработки в configtest.py
#   'inventory_data' название ФАЙЛА откуда берем данные лежащего в директории DATA

# Вариант параметризации через Pytest Mark Parameters:
def test_add_inventory_load_from_json_file(app, json_inventory_data ):

    inventory_item = json_inventory_data

    # 1. Открыть основное окно - так как оно может быть не открыто после другого теста.
    with allure.step(f'Open main window'):
        app.inventory.Open_main_window()

    # 2. Нажать на пункт меню Inventory и открыть на экране зону работы с инвентарем.
    with allure.step(f'Open inventory window'):
        app.inventory.Open_Inventory_window()

    # 3. Получим текущий список элементов:
    with allure.step(f'Get old list of inventory'):
        old_list = app.inventory.Get_inventory_list()

    # 4. Добавить новый элемент инвенторя (заполнить поля) и сохранить.
    with allure.step(f'Add new inventory item: Host={inventory_item.Inventory_Hostname} IPAddress={inventory_item.Inventory_IPaddress} Owner={inventory_item.Inventory_Owner} Purpose={inventory_item.Inventory_Purpose} HW={inventory_item.Inventory_Hardware} Notes={inventory_item.Inventory_Notes}'):
        NewInventory = Inventory(Inventory_Hostname  = inventory_item.Inventory_Hostname,
                             Inventory_IPaddress = inventory_item.Inventory_IPaddress,
                             Inventory_Owner     = inventory_item.Inventory_Owner,
                             Inventory_Purpose   = inventory_item.Inventory_Purpose,
                             Inventory_Hardware  = inventory_item.Inventory_Hardware,
                             Inventory_Notes     = inventory_item.Inventory_Notes)
        app.inventory.Add_new_inventory(NewInventory)

    # 5. Получим новый список элементов:
    with allure.step(f'Get new list of inventory'):
        new_list = app.inventory.Get_inventory_list()

    # 6. Добавим новый элемент в старый список чтобы списки стали равны:
    with allure.step(f'Add new inventory into old list'):
        old_list.append(NewInventory)

    # 7. Сравниваем списки применяя сортировку:
    with allure.step(f'Check Assert - lists comparation'):
        assert sorted(old_list) == sorted(new_list)

    # 8. Вернутся на главную страницу
    with allure.step(f'Return to main window'):
        app.inventory.Open_main_window()

########################################################################################################################################################################
# Тест проверяющий модификацию случайно выбранного существующего инвентаря (тестовых стендов)
########################################################################################################################################################################
# Вариант динамической параметризации pytest_generate_tests(metafunc)
# Имя параметра data_inventory_data формируется по правилам:
#   'data_' префикс для обработки в configtest.py
#   'inventory_data' название модуля откуда берем данные DATA.data_inventory
#
def test_modify_some_inventory(app, data_data_inventory):

    inventory_item = data_data_inventory

    # 1. Открыть основное окно - так как оно может быть не открыто после другого теста.
    with allure.step(f'Open main window'):
        app.inventory.Open_main_window()

    # 2. Нажать на пункт меню Inventory и открыть на экране зону работы с инвентарем.
    with allure.step(f'Open inventory window'):
        app.inventory.Open_Inventory_window()

    # 3. Проверим что есть уже хотя бы один элемент иначе нужно создать:
    with allure.step(f'Get quantity of inventory items on the screen'):
        len = app.inventory.count()

    with allure.step(f'If is zero? len = {len} (if 0 then add one inventory item)'):
        if len == 0:
            # 3.1 Добавить новый элемент инвенторя (заполнить поля) и сохранить.
            FirstInventory = Inventory(Inventory_Hostname="First inventory",
                                       Inventory_IPaddress="192.168.1.88",
                                       Inventory_Owner="testmanager",
                                       Inventory_Purpose="Testbed for somthing",
                                       Inventory_Hardware="Vegman R320",
                                       Inventory_Notes="создать единственный элемент для модификации если ничего нет'!")

            app.inventory.Add_new_inventory(FirstInventory)  # Создаем первый элемент чтобы было что модифицировать!
            len = 1

    # 4. Получим текущий список элементов:
    with allure.step(f'Get old list of inventory'):
        old_list = app.inventory.Get_inventory_list()

    # 5 Выбираем элемент для модификации в диапазоне от 0 до len:
    with allure.step(f'Get random index of inventory item for modification'):
        index = randrange(len)

    # 6. Указать обновляемые значения элемента инвенторя (заполнить поля) и сохранить.
    with allure.step(f'Set parameters for modification of inventory item: Host={inventory_item.Inventory_Hostname} IPAddress={inventory_item.Inventory_IPaddress} Owner={inventory_item.Inventory_Owner} Purpose={inventory_item.Inventory_Purpose} HW={inventory_item.Inventory_Hardware} Notes={inventory_item.Inventory_Notes}'):
        ModInventory = Inventory(Inventory_Hostname = inventory_item.Inventory_Hostname,
                                 Inventory_IPaddress = inventory_item.Inventory_IPaddress,
                                 Inventory_Owner = inventory_item.Inventory_Owner,
                                 Inventory_Purpose = inventory_item.Inventory_Purpose,
                                 Inventory_Hardware = inventory_item.Inventory_Hardware,
                                 Inventory_Notes= inventory_item.Inventory_Notes)

    # 7. Модифицировать элемент с номером index обновленными значениями
    with allure.step(f'Modify inventory item index={index}'):
        app.inventory.Modify_inventory_by_index(index, ModInventory)

    # 8. Получим новый список элементов:
    with allure.step(f'Get new list of inventory'):
        new_list = app.inventory.Get_inventory_list()

    # 9. Модифицируем элемент в старом списке чтобы списки стали равны:
    with allure.step(f'Change item with index={index}'):
        old_list[index] = ModInventory

    # 10. Сравниваем списки применяя сортировку:
    with allure.step(f'Check Assert - lists comparation'):
        assert sorted(old_list) == sorted(new_list)

    # 11. Вернутся на главную страницу
    with allure.step(f'Return to main window'):
        app.inventory.Open_main_window()


########################################################################################################################################################################
# Тест проверяющий удаление существующего инвентаря (тестовых стендов)
########################################################################################################################################################################

# Повторим тест 10 раз без входных параметров:
@pytest.mark.parametrize("_", range(20))
def test_delete_some_inventory(app, _):

    # 1. Открыть основное окно - так как оно может быть не открыто после другого теста.
    with allure.step(f'Open main window'):
        app.inventory.Open_main_window()

    # 2. Нажать на пункт меню Inventory и открыть на экране зону работы с инвентарем.
    with allure.step(f'Open inventory window'):
        app.inventory.Open_Inventory_window()

    # 3. Проверим что есть уже хотя бы один элемент иначе нужно создать:
    with allure.step(f'Get quantity of inventory items on the screen'):
        len = app.inventory.count()

    with allure.step(f'If is zero? len = {len} (if 0 then add one inventory item)'):
        if len == 0:
            # 3.1 Добавить новый элемент инвенторя (заполнить поля) и сохранить.
            FirtInventory = Inventory(Inventory_Hostname="New inventory",
                                      Inventory_IPaddress="192.168.1.77",
                                      Inventory_Owner="testmanager",
                                      Inventory_Purpose="Testbed for somthing",
                                      Inventory_Hardware="Vegman R320",
                                      Inventory_Notes="создать в теста модификации первого элемента!")

            app.inventory.Add_new_inventory(FirtInventory)  # Создаем первый элемент чтобы было что модифицировать!
            len = 1

    # 4. Получим текущий список элементов:
    with allure.step(f'Get old list of inventory'):
        old_list = app.inventory.Get_inventory_list()

    # 5 Выбираем случайный элемент для удаления в диапазоне от 0 до len:
    with allure.step(f'Get random index of inventory item for delete'):
        index = randrange(len)

    # 6. Удалить элемент инвентаря с индексом
    with allure.step(f'Delete random inventory item with index = {index}'):
        app.inventory.Delete_inventory_by_index(index)

    # 7. Получим новый список элементов:
    with allure.step(f'Get new list of inventory'):
        new_list = app.inventory.Get_inventory_list()

    # 8. Удаляем элемент с индексом index из старого списка чтобы списки стали равны:
    with allure.step(f'Delete item with index = {index} from old list'):
        old_list[index:index+1] = []

    # 9. Сравниваем списки применяя сортировку:
    with allure.step(f'Check Assert - lists comparation'):
        assert sorted(old_list) == sorted(new_list)

    # 10. Вернутся на главную страницу
    with allure.step(f'Return to main window'):
        app.inventory.Open_main_window()


    # Распечатаем оставшийся список если интересно:
    # list = app.inventory.Get_inventory_list()
    #
    # print("\n")
    # for element in list:
    #     print(element)
    #     print("\n")




