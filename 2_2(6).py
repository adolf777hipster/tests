from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.get("http://SunInJuly.github.io/execute_script.html")

x_element = browser.find_element_by_id('input_value').text


def calc():
    return str(math.log(abs(12 * math.sin(int(x_element)))))


button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

browser.find_element_by_id("answer").send_keys(calc())

browser.find_element_by_id("answer").send_keys(calc())
browser.find_element_by_css_selector("[for='robotCheckbox']").click()
browser.find_element_by_id("robotsRule").click()
browser.find_element_by_css_selector("[type = 'submit']").click()
