from selenium import webdriver
import os

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

name = browser.find_element_by_xpath('//div//*[@placeholder = "Введите имя"]').send_keys('Name')
second_name = browser.find_element_by_xpath('//div//*[@placeholder = "Введите фамилию"]').send_keys('Second name')
email = browser.find_element_by_xpath('//div//*[@placeholder = "Введите Email"]').send_keys('email@gmail.com')



current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt')
browser.find_element_by_name('file').send_keys(file_path)

browser.find_element_by_css_selector('[type="submit"]').click()

