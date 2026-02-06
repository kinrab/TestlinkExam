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
        driver.switch_to.default_content()                  # Восстанавливаем исходное позиционирование на весь документ
        driver.switch_to.frame("titlebar")                                        # Сначала нужно переключиться на фрейм
        driver.find_element(By.LINK_TEXT, "Logout").click()                       # Жми на кнопку! :-)

        # Все варианты нажать пункт меню Logout:
        # Сначала нужно переключиться на фрейм  driver.switch_to.frame("titlebar")
        # И потом уже нажать на кнопку!
        #driver.find_element(By.LINK_TEXT, "Logout").click()
        #driver.find_element(By.CSS_SELECTOR, "a[accesskey='q']").click()
        #driver.find_element(By.XPATH, "//a[@href='logout.php']").click()

