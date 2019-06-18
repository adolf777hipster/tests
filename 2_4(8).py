import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, 'price'), '10000'))
browser.find_element_by_id('book').click()
x_element = browser.find_element_by_id('input_value').text


def calc():
    return str(math.log(abs(12 * math.sin(int(x_element)))))


browser.find_element_by_name('text').send_keys(calc())

browser.find_element_by_css_selector('[type="submit"]').click()
