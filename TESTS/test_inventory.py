
from DATAMODEL.inventory_data import Inventory
from DATA.inventory_data import *
from random import randrange
import pytest

########################################################################################################################################################################
# Тест проверяющий создание нового инвентаря (тестовых стендов)
########################################################################################################################################################################

# Вариант параметризации через Pytest Mark Parameters:
@pytest.mark.parametrize("inventory_item", constant_data, ids =[repr(x) for x in constant_data ])
def test_add_inventory(app, inventory_item ):

    # 1. Открыть основное окно - так как оно может быть не открыто после другого теста.
    app.inventory.Open_main_window()

    # 2. Нажать на пункт меню Inventory и открыть на экране зону работы с инвентарем.
    app.inventory.Open_Inventory_window()

    # 3. Получим текущий список элементов:
    old_list = app.inventory.Get_inventory_list()

    # 4. Добавить новый элемент инвенторя (заполнить поля) и сохранить.
    NewInventory = Inventory(Inventory_Hostname  = inventory_item.Inventory_Hostname,
                             Inventory_IPaddress = inventory_item.Inventory_IPaddress,
                             Inventory_Owner     = inventory_item.Inventory_Owner,
                             Inventory_Purpose   = inventory_item.Inventory_Purpose,
                             Inventory_Hardware  = inventory_item.Inventory_Hardware,
                             Inventory_Notes     = inventory_item.Inventory_Notes)

    app.inventory.Add_new_inventory(NewInventory)

    # 5. Получим новый список элементов:
    new_list = app.inventory.Get_inventory_list()

    # 6. Добавим новый элемент в старый список чтобы списки стали равны:
    old_list.append(NewInventory)

    # 7. Сравниваем списки применяя сортировку:
    assert sorted(old_list) == sorted(new_list)

    # 8. Вернутся на главную страницу
    app.inventory.Open_main_window()


########################################################################################################################################################################
# Тест проверяющий модификацию случайно выбранного существующего инвентаря (тестовых стендов)
########################################################################################################################################################################

# Вариант параметризации через Pytest Mark Parameters:
@pytest.mark.parametrize("inventory_item", test_data, ids =[repr(x) for x in test_data ])
def test_modify_some_inventory(app, inventory_item):

    # 1. Открыть основное окно - так как оно может быть не открыто после другого теста.
    app.inventory.Open_main_window()

    # 2. Нажать на пункт меню Inventory и открыть на экране зону работы с инвентарем.
    app.inventory.Open_Inventory_window()

    # 3. Проверим что есть уже хотя бы один элемент иначе нужно создать:
    len = app.inventory.count()

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
    old_list = app.inventory.Get_inventory_list()

    # 5 Выбираем элемент для модификации в диапазоне от 0 до len:
    index = randrange(len)

    # 6. Указать обновляемые значения элемента инвенторя (заполнить поля) и сохранить.
    ModInventory = Inventory(Inventory_Hostname=inventory_item.Inventory_Hostname,
                             Inventory_IPaddress=inventory_item.Inventory_IPaddress,
                             Inventory_Owner=inventory_item.Inventory_Owner,
                             Inventory_Purpose=inventory_item.Inventory_Purpose,
                             Inventory_Hardware=inventory_item.Inventory_Hardware,
                             Inventory_Notes=inventory_item.Inventory_Notes)

    # 7. Модифицировать элемент с номером index обновленными значениями
    app.inventory.Modify_inventory_by_index(index, ModInventory)

    # 8. Получим новый список элементов:
    new_list = app.inventory.Get_inventory_list()

    # 9. Модифицируем элемент в старом списке чтобы списки стали равны:
    old_list[index] = ModInventory

    # 10. Сравниваем списки применяя сортировку:
    assert sorted(old_list) == sorted(new_list)

    # 11. Вернутся на главную страницу
    app.inventory.Open_main_window()


########################################################################################################################################################################
# Тест проверяющий удаление существующего инвентаря (тестовых стендов)
########################################################################################################################################################################

# Повторим тест 10 раз без входных параметров:
@pytest.mark.parametrize("_", range(10))
def test_delete_some_inventory(app, _):

    # 1. Открыть основное окно - так как оно может быть не открыто после другого теста.
    app.inventory.Open_main_window()

    # 2. Нажать на пункт меню Inventory и открыть на экране зону работы с инвентарем.
    app.inventory.Open_Inventory_window()

    # 3. Проверим что есть уже хотя бы один элемент иначе нужно создать:
    len = app.inventory.count()

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
    old_list = app.inventory.Get_inventory_list()

    # 4 Выбираем элемент для удаления в диапазоне от 0 до len:
    index = randrange(len)

    # 5. Удалить элемент инвентаря с индексом
    app.inventory.Delete_inventory_by_index(index)

    # 6. Получим новый список элементов:
    new_list = app.inventory.Get_inventory_list()

    # 7. Удаляем элемент с индексом index из старого списка чтобы списки стали равны:
    old_list[index:index+1] = []

    # 8. Сравниваем списки применяя сортировку:
    assert sorted(old_list) == sorted(new_list)

    # 6. Вернутся на главную страницу
    app.inventory.Open_main_window()


    # Распечатаем оставшийся список если интересно:
    # list = app.inventory.Get_inventory_list()
    #
    # print("\n")
    # for element in list:
    #     print(element)
    #     print("\n")




