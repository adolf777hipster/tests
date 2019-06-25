import unittest
from selenium import webdriver
import time



class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # name
        browser.find_element_by_xpath('//div//*[@placeholder = "Введите имя"]').send_keys('Name')
        # second_name
        browser.find_element_by_xpath('//div//*[@placeholder = "Введите фамилию"]').send_keys(
            'Second name')
        # email
        browser.find_element_by_xpath('//div//*[@placeholder = "Введите Email"]').send_keys('email@gmail.com')
        # button
        browser.find_element_by_css_selector("button.btn").click()

        time.sleep(1)

        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", browser.find_element_by_tag_name("h1").text,
                         "Should be equal")

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # name
        browser.find_element_by_xpath('//div//*[@placeholder = "Введите имя"]').send_keys('Name')
        # second_name
        browser.find_element_by_xpath('//div//*[@placeholder = "Введите фамилию"]').send_keys(
            'Second name')
        # email
        browser.find_element_by_xpath('//div//*[@placeholder = "Введите Email"]').send_keys('email@gmail.com')
        # button
        browser.find_element_by_css_selector("button.btn").click()

        time.sleep(1)

        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", browser.find_element_by_tag_name("h1").text,
                         "Should be equal")


if __name__ == "__main__":
    unittest.main()
