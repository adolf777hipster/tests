from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")

x_element = browser.find_element_by_id('input_value').text


def calc():
    return str(math.log(abs(12 * math.sin(int(x_element)))))


y = calc()


browser.find_element_by_id("answer").send_keys(y)

browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_css_selector("[for='robotCheckbox']").click()
browser.find_element_by_id("robotsRule").click()
browser.find_element_by_css_selector("[type = 'submit']").click()
