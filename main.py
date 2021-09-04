import sys
import unittest
import Authorization
import CountMessages
import SendMessage
from selenium import webdriver

class TestTask(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor=host, # Нужно хардкодить
            desired_capabilities={
                'browserName': browserName # Нужно хардкодить
            }
        )

    def test_run(self):
        auth = Authorization.Authorization(self.driver)
        auth.auth()

        cm = CountMessages.CountMessages(auth.driver)
        cm.count_messages()

        sm = SendMessage.SendMessage(cm.driver, browserName) # Нужно хардкодить
        sm.send_message(cm.count)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    browserName = sys.argv[1]
    host = sys.argv[2]

    unittest.main()