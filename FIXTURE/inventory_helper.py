from selenium.common.exceptions import NoSuchElementException # Важный импорт
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from DATAMODEL.inventory_data_model import Inventory
from selenium.webdriver.common.by import By
import allure

########################################################################################################################################################################################
# Класс для реализации всех вспомогательных методов работающих с сущностью Inventory (testbeds)
########################################################################################################################################################################################

class InventoryHelper:

    inventory_cash = None

    #################################################################################################################################################
    # Конструктор класса InventoryHelper
    #################################################################################################################################################

    def __init__(self, app):

        self.app = app

    ##################################################################################################################################################
    # Метод добавляющий новый инвентарь - тестовый стенд
    ##################################################################################################################################################
    @allure.step(f"Add_new_inventory")
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

        # Если нужно вернуться назад: # driver.switch_to.window(original_window) - но не нужно - окно само закрывается!

        # 5. Выходим на основную страницу
        driver.switch_to.default_content()                  # Восстанавливаем исходное позиционирование на весь документ

        self.inventory_cash = None

    ##################################################################################################################################################
    # Метод модификирующий первый в списке инвентарь - тестовый стенд
    ##################################################################################################################################################
    @allure.step("Modify_first_inventory")
    def Modify_first_inventory(self, new_inventory):

        self.Modify_inventory_by_index(0, new_inventory)

    ##################################################################################################################################################
    # Метод модификирующий первый в списке инвентарь - тестовый стенд
    ##################################################################################################################################################
    @allure.step("Modify_inventory_by_index index={index}")
    def Modify_inventory_by_index(self, index, new_inventory):

        # 1. В переменную driver передаем драйвер из фикстуры Application
        driver = self.app.driver

        # 2. Кликнуть на элемент в списке заданный индексом:
        self.Select_Inventory_By_Index(index)

        # 3. Нажать на кнопку Edit

        # 3.1 Open modification window - кнопку Edit нажать     <button type="button" id="ext-gen27"
        driver.find_element(By.ID, "ext-gen25").click()

        # 3.2 Открывается окно c атрибутами выбранного элемента:

        # 4. Заполняем фррму новыми значениями:
        self.Fill_inventory_form(new_inventory)

        # 5. Нажимаем кнопку Yes                 <button type="button" id="ext-gen48" class=" x-btn-text">Save</button>

        # 6. Сохраняем ID текущего окна
        original_window = driver.current_window_handle

        # 7. Получаем список всех открытых окон и переключаемся на последнее
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        # 8. Теперь можно искать кнопку
        driver.find_element(By.XPATH, "//button[text()='Save']").click()

        # Если нужно вернуться назад: # driver.switch_to.window(original_window) - но не нужно - окно само закрывается!

        # 9. Восстанавливаем исходное позиционирование на весь документ
        driver.switch_to.default_content()

        self.inventory_cash = None

    ##################################################################################################################################################
    # Метод удаляющий первый в списке инвентарь - тестовый стенд
    ##################################################################################################################################################
    @allure.step("Delete_first_inventory")
    def Delete_first_inventory(self):

        self.Delete_inventory_by_index(0)

    ##################################################################################################################################################
    # Метод возвращающий список всех элементов inventory со всем параметрами:
    ##################################################################################################################################################
    @allure.step("Get_inventory_list")
    def Get_inventory_list(self):

        if self.inventory_cash is None:
            driver = self.app.driver
            self.inventory_cash = []

            driver.switch_to.frame("mainframe")

            # 1. Забираем ВСЕ ячейки одним запросом.
            # Селектор ищет все div с нужными классами внутри таблиц строк.
            cells = driver.find_elements(By.XPATH,"//table[@class='x-grid3-row-table']//div[contains(@class, 'x-grid3-col-') and @unselectable='on']")

            # 2. Итерируемся по списку с шагом 6 (количество колонок)
            for i in range(0, len(cells), 6):
                # Берем срез из 6 элементов для текущей строки
                row_cells = cells[i:i + 6]

                # Предварительно извлекаем текст, чтобы не обращаться к .text в конструкторе многократно
                # (Это еще немного ускорит процесс)
                t = [cell.text for cell in row_cells]

                self.inventory_cash.append(Inventory(
                    Inventory_Hostname=t[0],
                    Inventory_IPaddress=t[1],
                    Inventory_Purpose=t[2],
                    Inventory_Hardware=t[3],
                    Inventory_Owner=t[4],
                    Inventory_Notes=t[5]
                ))

            driver.switch_to.default_content()

        return list(self.inventory_cash)



        # Мой исходный неоптимальный вариант:
        # if self.inventory_cash is None:
        #
        #     # 1. В переменную driver передаем драйвер из фикстуры Application
        #     driver = self.app.driver
        #
        #     # 3. Объяаляем пустой список для сохранения элементов
        #     self.inventory_cash = []
        #
        #     # 4. Сначала нужно переключиться на фрейм:
        #     driver.switch_to.frame("mainframe")
        #
        #     # 5. Проходим по всем элементам inventory на странице
        #     for row in driver.find_elements(By.XPATH, "//table[@class='x-grid3-row-table']"):
        #
        #         # 5.1 Ищем и получаем значение атрибута Hostname в Inventory
        #         hostname = row.find_element(By.XPATH, ".//div[contains(@class, 'x-grid3-col-0') and @unselectable='on']")
        #
        #         # 5.2 Ищем и получаем значение атрибута IPaddress в Inventory
        #         ipaddress = row.find_element(By.XPATH, ".//div[contains(@class, 'x-grid3-col-1') and @unselectable='on']")
        #
        #         # 5.3 Ищем и получаем значение атрибута Purpose в Inventory
        #         purpose = row.find_element(By.XPATH, ".//div[contains(@class, 'x-grid3-col-2') and @unselectable='on']")
        #
        #         # 5.4 Ищем и получаем значение атрибута Hardware в Inventory
        #         hardware = row.find_element(By.XPATH, ".//div[contains(@class, 'x-grid3-col-3') and @unselectable='on']")
        #
        #         # 5.5 Ищем и получаем значение атрибута Owner в Inventory
        #         owner = row.find_element(By.XPATH, ".//div[contains(@class, 'x-grid3-col-4') and @unselectable='on']")
        #
        #         # 5.6 Ищем и получаем значение атрибута Notes в Inventory
        #         notes = row.find_element(By.XPATH, ".//div[contains(@class, 'x-grid3-col-5') and @unselectable='on']")
        #
        #         self.inventory_cash.append( Inventory ( Inventory_Hostname = hostname.text, Inventory_IPaddress = ipaddress.text, Inventory_Owner = owner.text,
        #                                            Inventory_Purpose = purpose.text, Inventory_Hardware = hardware.text, Inventory_Notes = notes.text ) )
        #
        #     # End for
        #
        #     # 5. Восстанавливаем исходное позиционирование на весь документ
        #     driver.switch_to.default_content()
        #
        # return list(self.inventory_cash)

    ##################################################################################################################################################
    # Метод возвращающий число элементов инвентаря
    ##################################################################################################################################################
    @allure.step("count")
    def count(self):

        # 1. В переменную driver передаем драйвер из фикстуры Application
        driver = self.app.driver

        # 2. Сначала нужно переключиться на фрейм:
        driver.switch_to.frame("mainframe")

        # 3. Посчитать количество контактов:

        #  Старый способ не очень быстрый: count = len( driver.find_elements(By.XPATH, "//table[@class='x-grid3-row-table']") )

        #  Считаем количество через выполнение JS кода (это самый быстрый способ)
        #  Вместо того чтобы тянуть все объекты в Python, мы попросим браузер вернуть только одно число.
        count = driver.execute_script("return document.querySelectorAll('table.x-grid3-row-table').length;")

        # 4. Восстанавливаем исходное позиционирование на весь документ
        driver.switch_to.default_content()

        return count

    ##################################################################################################################################################
    # Метод удаляющий элемент инвентаря по индексу
    ##################################################################################################################################################
    @allure.step(" Delete_inventory_by_index index={index}")
    def Delete_inventory_by_index(self, index):

        # 1. В переменную driver передаем драйвер из фикстуры Application
        driver = self.app.driver

        # 2. Кликнуть на элемент в списке заданный индексом:
        self.Select_Inventory_By_Index(index)

        # 3. Нажать на кнопку Delete

        # 3.1 Open modification window - кнопку Delete нажать     <button type="button" id="ext-gen27"
        driver.find_element(By.ID, "ext-gen27").click()

        # Открывается окно с вопросами - подтвердить удаление и кнопками YES NO

        # 3.2 Нажимаем кнопку Yes                 <button type="button" id="ext-gen48" class=" x-btn-text">Save</button>

        # 3.3 Сохраняем ID текущего окна
        original_window = driver.current_window_handle

        # 3.4 Получаем список всех открытых окон и переключаемся на последнее
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        # 3.5 Теперь можно искать кнопку
        driver.find_element(By.XPATH, "//button[text()='Yes']").click()

        # Если нужно вернуться назад: # driver.switch_to.window(original_window) - но не нужно - окно само закрывается!


        # 4. Восстанавливаем исходное позиционирование на весь документ
        driver.switch_to.default_content()

        self.inventory_cash = None

    ##################################################################################################################################################
    # Метод выбирает на экране инвентаря нужный элемент по индексу (считая сверху - вниз)
    ##################################################################################################################################################
    @allure.step("Select_Inventory_By_Index index={index}")
    def Select_Inventory_By_Index(self, index):

        # 1. В переменную driver передаем драйвер из фикстуры Application
        driver = self.app.driver

        # 2. Сначала нужно переключиться на фрейм
        driver.switch_to.frame("mainframe")

        # 3. Проходим по списку всех найденных элементов и ищем нужный:

        # Вариант через Xpath и явным ожиданием:
        # явное ожидание(WebDriverWait), чтобы код не падал, если таблица загружается с задержкой

        # 1. Формируем тот самый рабочий XPath
        xpath_selector = f"(//table[@class='x-grid3-row-table'])[{index + 1}]"

        # 2. Ждем до 10 секунд, пока элемент не только появится, но и станет кликабельным
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_selector)))

        # 3. Кликаем
        element.click()

        # Старый способ не оптимальный очень! Лушче сразу по индексу мы
        # i = 0
        # for row in driver.find_elements(By.XPATH, "//table[@class='x-grid3-row-table']"):
        #     if i == index:                                                                    # Мы нашли искомый элемент
        #         row.click()
        #         break                                                                             # Можно завершать цикл
        #     i = i + 1

        return

    ##################################################################################################################################################
    # Метод изменяющий атрибут инвентаря если он не пустой
    ##################################################################################################################################################
    @allure.step("Change_Field_Value value={text_value} fiedlname={field_name}")
    def Change_Field_Value(self, text_value, field_name):

        driver = self.app.driver

        if field_name == "editOwner":

            # Если поле выпадающий список:
            if text_value is not None:

                # 3.3 Заполняем поле owner:
                driver.find_element(By.ID, "editOwner").click()
                dropdown = driver.find_element(By.ID, "editOwner")
                dropdown.find_element(By.XPATH,"//div[contains(@class, 'x-combo-list-item') and text()='%s']" %  text_value  ).click()

        else:  # Если обычное поле:
            if text_value is not None:
                driver.find_element(By.ID, field_name).click()
                driver.find_element(By.ID, field_name).clear()
                driver.find_element(By.ID, field_name).send_keys(text_value)

    ####################################################################################################################
    # Метод заполняющий все поля элемента инвентаря
    ####################################################################################################################
    @allure.step("Fill_inventory_form")
    def Fill_inventory_form(self, inventory_item):

        self.Change_Field_Value(inventory_item.Inventory_Hostname, "editName")
        self.Change_Field_Value(inventory_item.Inventory_IPaddress, "editIp")
        self.Change_Field_Value(inventory_item.Inventory_Owner, "editOwner")
        self.Change_Field_Value(inventory_item.Inventory_Purpose, "editPurpose")
        self.Change_Field_Value(inventory_item.Inventory_Hardware, "editHw")
        self.Change_Field_Value(inventory_item.Inventory_Notes, "editNotes")

    ####################################################################################################################
    # Метод добавляющий новый инвеинтарь - тестовый стенд
    ####################################################################################################################
    @allure.step(" Open_main_window")
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
    @allure.step("Open_Inventory_window")
    def Open_Inventory_window(self):

        # 1. В переменную driver передаем драйвер из фикстуры Application
        driver = self.app.driver

        # 2. Ищем элемент <h1 class="title">Inventory</h1>
        try:
            driver.switch_to.frame("mainframe")                                    # Сначала нужно переключиться на фрейм
            element = driver.find_element(By.CSS_SELECTOR, "h1.title") # Если элемент есть, то мы уже на нужной странице
            if element is not None:
                driver.switch_to.default_content()          # Восстанавливаем исходное позиционирование на весь документ
                return                                      #                     И уходим так как все что нужно сделали
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








