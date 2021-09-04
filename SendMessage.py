from selenium import webdriver

class SendMessage:
    def __init__(self, driver, browserName):
        self.driver = driver
        self.browser = browserName

    def send_message(self, count):
        # Нажимаем на кнопку, чтобы написать письмо
        self.driver.find_element_by_link_text("Написать").click()

        # Печатаем получателя письма
        address = self.driver.find_element_by_class_name('composeYabbles')
        address.send_keys('Shamilov.ilsh@yandex.ru')

        # Перекидываем курсор, на следущую строку нажатием ENTER (чтобы обойти наложение всплывающего окна)
        if self.browser == 'firefox':
            address.send_keys(u'\ue007')

        # Печатаем тему письма
        subject = self.driver.find_element_by_name('subject')
        subject.send_keys('Simbirsoft Тестовое задание. Шамилов.')

        # Печатаем содержимое письма
        content_div = self.driver.find_element_by_id('cke_1_contents')
        letter_content = content_div.find_element_by_xpath(
            "div[@class='cke_wysiwyg_div cke_reset cke_enable_context_menu cke_editable cke_editable_themed cke_contents_ltr cke_htmlplaceholder']/div/br")

        # Пацан к успеху шел, наложение встретил и ушел :(
        # Тут перепробовал все, но постоянно ловил "element is not reachable by keyboard", а все из-за всплывающего окна автозаполнения
        # Поэтому для firefox содержание письма игнорируется
        if self.browser != 'firefox':
            letter_content.send_keys('Количество входящих с данной темой: ' + str(count))