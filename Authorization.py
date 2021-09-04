from selenium import webdriver

class Authorization:
    def __init__(self, driver):
        self.driver = driver

    def auth(self):
        self.driver.implicitly_wait(20)
        #Переходим на страницу авторизации
        self.driver.get("https://mail.yandex.ru//")

        self.driver.find_element_by_link_text("Войти").click()

        #Вводим логин
        login = self.driver.find_element_by_id('passp-field-login')
        login.send_keys('login')
        self.driver.find_element_by_id('passp:sign-in').click()

        #Вводим пароль
        password = self.driver.find_element_by_id('passp-field-passwd')
        password.send_keys('password')
        self.driver.find_element_by_id('passp:sign-in').click()

