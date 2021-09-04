from selenium import webdriver

class CountMessages:
    def __init__(self, driver):
        self.driver = driver
        self.count = 0

    def count_messages(self):
        # Находим блок div, в котором лежат все сообщения
        div = self.driver.find_element_by_xpath("//div[@class='ns-view-container-desc mail-MessagesList js-messages-list']")

        # Циклом обрабатываем текущую директорию и подсчитывает количество нужных нам сообщений
        for item in div.find_elements_by_xpath("./div"):
            temp = item.find_element_by_xpath(
                ".//span[@class='mail-MessageSnippet-Item mail-MessageSnippet-Item_subject']/span[1]")
            if (temp.text == "Simbirsoft Тестовое задание"):
                self.count += 1