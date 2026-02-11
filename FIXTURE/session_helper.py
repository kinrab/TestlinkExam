from selenium.common.exceptions import NoSuchElementException # Важный импорт
from selenium.webdriver.common.by import By
import allure

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
    @allure.step("Login_process user={username} password={password}")
    def Login_process(self, username, password):

        # 1. Передаем ссылку на Selenium драйвер:
        driver = self.app.driver

        # Открыть страницу приложения!
        #driver.get(self.app.base_url)

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
    @allure.step("Logout_process")
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

    ####################################################################################################################
    # Функция проверочного лиогина
    ####################################################################################################################
    @allure.step("Ensure_login user={username} password={password}")
    def Ensure_Login(self, username, password):

        # 0. Передаем ссылку на app и драйвер:
        driver = self.app.driver
        app = self.app

        # 1. Открыть ссылку на testlink только при первом запуске браузера!
        str = app.base_url + "index.php"
        if driver.current_url != str:
            driver.get(app.base_url)

        # 2. Проверим залогинены мы или нет?
        Flag = self.Is_Logged_In()

        # в идеале добавить проверку на совпадение имени пользолвателя и релогин если имя пользователя другое!

        # 3. Если залогинены то можно уходить
        if Flag is True:
            return

        self.Login_process(username, password)

    ####################################################################################################################
    # Функция проверочного логаута и завершения сессии:
    ####################################################################################################################
    @allure.step("Ensure_logout")
    def Ensure_logout(self):

        # 1. Проверим залогинены мы или нет?
        Flag = self.Is_Logged_In()

        # 2. Если не залогинены то можно уходить
        if Flag is False:
            return

        self.Logout_process()

    ####################################################################################################################
    # Функция проверяет что мы внутри сессии польователя:
    ####################################################################################################################
    @allure.step("Is_Logged_In")
    def Is_Logged_In(self):

        # 1. Передаем ссылку на Selenium драйвер:
        driver = self.app.driver

        # 3. Проверяем наличие элемента на странице    <span class ="bold"> TestLink 1.9 (Prague): admin[admin] </span>
        try:
            element = driver.find_element(By.XPATH, "//div[@class='fullpage_head' and contains(., 'TestLink 1.9')]")
            if element is not None:
                return False                                                    # Возвращаемся - Мы НЕ ЗАЛОГИНЕНЫ!

        except NoSuchElementException:
            pass

        return True                                                             # Иначе - МЫ ЗАЛОГИНЕНЫ!