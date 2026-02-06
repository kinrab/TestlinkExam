
from DATAMODEL.inventory_data import Inventory

########################################################################################################################################################################
# Тест проверяющий создание нового инвентаря (тестовых стендов)
########################################################################################################################################################################

def test_add_inventory(app):

    # 1. Открыть основное окно - так как оно может быть не открыто после другого теста.
    app.inventory.Open_main_window()

    # 2. Нажать на пункт меню Inventory и открыть на экране зону работы с инвентарем.
    app.inventory.Open_Inventory_window()

    # 3. Добавить новый элемент инвенторя (заполнить поля) и сохранить.
    NewInventory = Inventory(Inventory_Hostname = "Toetomi Hideyosi",
                             Inventory_IPaddress = "192.168.1.100",
                             Inventory_Owner = "testmanager",
                             Inventory_Purpose = "Testbed for integration testing",
                             Inventory_Hardware = "Vegman R220",
                             Inventory_Notes = "Не выключать на ночь!")

    app.inventory.Add_new_inventory(NewInventory)

    #4. Вернутся на главную страницу
    app.inventory.Open_main_window()

