from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")
window_before = browser.window_handles[0]

browser.find_element_by_css_selector('[type = "submit"]').click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x_element = browser.find_element_by_id('input_value').text


def calc():
    return str(math.log(abs(12 * math.sin(int(x_element)))))


browser.find_element_by_name('text').send_keys(calc())

browser.find_element_by_css_selector('[type="submit"]').click()
