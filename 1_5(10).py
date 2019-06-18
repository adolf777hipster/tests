from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

name = browser.find_element_by_xpath('//div//*[@placeholder = "Введите имя"]').send_keys('Name')
second_name = browser.find_element_by_xpath('//div//*[@placeholder = "Введите фамилию"]').send_keys('Second name')
email = browser.find_element_by_xpath('//div//*[@placeholder = "Введите Email"]').send_keys('email@gmail.com')

button = browser.find_element_by_css_selector("button.btn").click()

time.sleep(1)

assert "Поздравляем! Вы успешно зарегистировались!" == browser.find_element_by_tag_name("h1").text
