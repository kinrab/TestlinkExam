from selenium.common.exceptions import NoSuchElementException # Важный импорт
from selenium.webdriver.common.by import By


########################################################################################################################################################################################
# Класс для реализации всех вспомогательных методов работающих с сущностью Inventory (testbeds)
########################################################################################################################################################################################

class InventoryHelper:

    #################################################################################################################################################
    # Конструктор класса InventoryHeler
    #################################################################################################################################################

    def __init__(self, app):

        self.app = app

    ##################################################################################################################################################
    # Метод добавляющий новый инвеинарь - тестовый стенд
    ##################################################################################################################################################

    def Add_new_inventory(self,new_inventory):

        # 1. В переменную driver передаем драйвер из фикстуры Application
        driver = self.app.driver

        # 2. Нажимаем кнопку Create:                       <button type="button" id="ext-gen23" class=" x-btn-text icon_device_create">Create</button>
        driver.switch_to.frame("mainframe")                                      # Сначала нужно переключиться на фрейм в котором размещается кнопка!
        driver.find_element(By.XPATH, "//button[text()='Create']").click()

        # 3. Заполняем все поля нового элемента Inventory

        # 3.1 Заполняем поле host name:
        driver.find_element(By.ID, "editName").click()
        driver.find_element(By.ID, "editName").clear()
        driver.find_element(By.ID, "editName").send_keys(new_inventory.Inventory_Hostname)

        # 3.2 Заполняем поле IP address:
        driver.find_element(By.ID, "editIp").click()
        driver.find_element(By.ID, "editIp").clear()
        driver.find_element(By.ID, "editIp").send_keys(new_inventory.Inventory_IPaddress)

        # 3.3 Заполняем поле owner:
        driver.find_element(By.ID, "editOwner").click()
        dropdown = driver.find_element(By.ID, "editOwner")
        dropdown.find_element(By.XPATH, "//div[contains(@class, 'x-combo-list-item') and text()='testmanager']").click()

        # 3.4 Заполняем поле Purpose:
        driver.find_element(By.ID, "editPurpose").click()
        driver.find_element(By.ID, "editPurpose").clear()
        driver.find_element(By.ID, "editPurpose").send_keys(new_inventory.Inventory_Purpose)

        # 3.5 Заполняем поле Hardware:
        driver.find_element(By.ID, "editHw").click()
        driver.find_element(By.ID, "editHw").clear()
        driver.find_element(By.ID, "editHw").send_keys(new_inventory.Inventory_Hardware)

        # 3.1 Заполняем поле Notes:
        driver.find_element(By.ID, "editNotes").click()
        driver.find_element(By.ID, "editNotes").clear()
        driver.find_element(By.ID, "editNotes").send_keys(new_inventory.Inventory_Notes)

        # 4. Нажимаем кнопку Save                 <button type="button" id="ext-gen48" class=" x-btn-text">Save</button>

        # 4.1 Сохраняем ID текущего окна
        original_window = driver.current_window_handle

        # 4.2 Получаем список всех открытых окон и переключаемся на последнее
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        # 4.3 Теперь можно искать кнопку
        driver.find_element(By.XPATH, "//button[text()='Save']").click()

        # Если нужно вернуться назад: # driver.switch_to.window(original_window)


        # 5. Выходим на основную страницу
        driver.switch_to.default_content()                  # Восстанавливаем исходное позиционирование на весь документ

    ####################################################################################################################
    # Метод добавляющий новый инвеинарь - тестовый стенд
    ####################################################################################################################

    def Open_main_window(self):

        # 1. В переменную driver передаем драйвер из фикстуры Application
        driver = self.app.driver

        # 2. Ищем элемент: Current Test Plan: <form name="testplanForm" action="lib/general/mainPage.php">
        try:
            driver.switch_to.frame("mainframe")                                   # Сначала нужно переключиться на фрейм
            element = driver.find_element(By.CSS_SELECTOR,"form[name='testplanForm'][action='lib/general/mainPage.php']")
            if element is not None:                                    # Если элемент есть, то мы уже на нужной странице
                driver.switch_to.default_content()          # Восстанавливаем исходное позиционирование на весь документ
                return
        except NoSuchElementException:
            pass

        # 4. Иначе кликаем на пункт меню <a href="index.php" target="_parent" accesskey="h" tabindex="" 1''="">Project</a>
        driver.switch_to.default_content()                  # Восстанавливаем исходное позиционирование на весь документ
        driver.switch_to.frame("titlebar")  # Сначала нужно переключиться на фрейм
        driver.find_element(By.LINK_TEXT, "Project").click()

        # 5. Восстанавливаем исходное позиционирование на весь документ
        driver.switch_to.default_content()
        return

    ####################################################################################################################
    # Метод добавляющий новый инвеинарь - тестовый стенд
    ####################################################################################################################

    def Open_Inventory_window(self):

        # 1. В переменную driver передаем драйвер из фикстуры Application
        driver = self.app.driver

        # 2. Ищем элемент <h1 class="title">Inventory</h1>
        try:
            driver.switch_to.frame("titlebar")  # Сначала нужно переключиться на фрейм
            element = driver.find_element(By.CSS_SELECTOR, "h1.title") # Если элемент есть, то мы уже на нужной странице
            if element is not None:
                driver.switch_to.default_content()          # Восстанавливаем исходное позиционирование на весь документ
                return
        except NoSuchElementException:
            pass

        # 3. Иначе кликаем на пункт меню Inventory
        driver.switch_to.default_content()                  # Восстанавливаем исходное позиционирование на весь документ
        driver.switch_to.frame("mainframe")                                       # Сначала нужно переключиться на фрейм
        driver.find_element(By.LINK_TEXT, "Inventory").click()

        # 4. Восстанавливаем исходное позиционирование на весь документ
        driver.switch_to.default_content()
        return

########################################################################################################################################################################################
# Конец описания класса для реализации всех вспомогательных методов работающих с сущностью Inventory (testbeds)
########################################################################################################################################################################################








