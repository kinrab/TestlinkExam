from selenium.webdriver.common.by import By
import time

# Класс описывающий сущность Сессия с логином и логаутом
class SessionHelper:

    ####################################################################################################################
    # Контруктор класса
    ####################################################################################################################

    def __init__(self,app):

        self.app = app

    ####################################################################################################################
    # Функция логина в сессию:
    ####################################################################################################################

    def Login_process(self, username, password):

        # 1. Передаем ссылку на Selenium драйвер:
        driver = self.app.driver

        # Открыть страницу приложения!
        driver.get(self.app.base_url)

        # Ввод в поле логина admin
        driver.find_element(By.NAME, "tl_login").click()
        driver.find_element(By.NAME, "tl_login").clear()
        driver.find_element(By.NAME, "tl_login").send_keys(username)

        # Ввод в поле пароля secret
        driver.find_element(By.NAME, "tl_password").click()
        driver.find_element(By.NAME, "tl_password").clear()
        driver.find_element(By.NAME, "tl_password").send_keys(password)

        # Debug only
        #time.sleep(3) # Посмотрим 3 секунды до нажатия кнопки, что все заполнено правильно

        # Нажать на кнопку "Войти"
        driver.find_element(By.NAME, "login_submit").click()

        # Все варианты нажать кнопку "Войти"
        #driver.find_element(By.NAME, "login_submit").click()
        #driver.find_element(By.XPATH, "//input[@value='Войти']").click()
        #driver.find_element(By.CSS_SELECTOR, "input[name='login_submit']").click()




    ####################################################################################################################
    # Функция логаута и завершения сессии:
    ####################################################################################################################
    def Logout_process(self):

        # 0. Только для отладки фикстуры в первых запусках:
        #time.sleep(3)

        # 1. Передаем ссылку на Selenium драйвер:
        driver = self.app.driver

        #2. Выполнить действие логаута:  # <a href="logout.php" target="_parent" accesskey="q">Logout</a>
        driver.switch_to.frame("titlebar")                                        # Сначала нужно переключиться на фрейм
        driver.find_element(By.LINK_TEXT, "Logout").click()                       # Жми на кнопку! :-)

        # Все варианты нажать пункт меню Logout:
        # Сначала нужно переключиться на фрейм  driver.switch_to.frame("titlebar")
        # И потом уже нажать на кнопку!
        #driver.find_element(By.LINK_TEXT, "Logout").click()
        #driver.find_element(By.CSS_SELECTOR, "a[accesskey='q']").click()
        #driver.find_element(By.XPATH, "//a[@href='logout.php']").click()

    # def Ensure_Logout_process(self):
    #
    #     #driver = self.app.driver
    #
    #     if  self.Is_Logged_In():
    #
    #         self.Logout_process()
    #
    #
    # def Is_Logged_In(self):
    #
    #     #print("Is_Logged_In:\n ")
    #
    #     driver = self.app.driver
    #
    #     num = len( driver.find_elements(By.LINK_TEXT, "Logout") )
    #
    #     #print("Num = ", str(num) )
    #
    #     return num > 0
    #
    #
    # def Is_Logged_In_As(self, username):
    #
    #     driver = self.app.driver
    #
    #     item = driver.find_element(By.XPATH, "//div/div[1]/form/b")
    #
    #     #print("Item: " + item.text + "\n" )
    #
    #     return  item.text == "(" + username+ ")"
    #
    #
    # def Ensure_Login_process(self, username, password):
    #
    #     # Открыть страницу приложения!
    #     self.Open_Home_Page()
    #
    #     Flag = self.Is_Logged_In()
    #
    #     if  Flag is True:
    #
    #         if self.Is_Logged_In_As(username):
    #             return
    #         else:
    #             self.Logout_process()
    #
    #     self.Login_process(username,password)
