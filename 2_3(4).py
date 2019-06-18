from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

browser.find_element_by_css_selector('[type = "submit"]').click()

alert = browser.switch_to.alert
alert.accept()

x_element = browser.find_element_by_id('input_value').text


def calc():
    return str(math.log(abs(12 * math.sin(int(x_element)))))


browser.find_element_by_name('text').send_keys(calc())

browser.find_element_by_css_selector('[type="submit"]').click()
