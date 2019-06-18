from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")

x_element = browser.find_element_by_id('treasure').get_attribute('valuex')
print(x_element)

def calc():
    return str(math.log(abs(12 * math.sin(int(x_element)))))


browser.find_element_by_id("answer").send_keys(calc())

browser.find_element_by_id("answer").send_keys(calc())
browser.find_element_by_id("robotCheckbox").click()
browser.find_element_by_id("robotsRule").click()
browser.find_element_by_css_selector("[type = 'submit']").click()
