from selenium import webdriver
import math

link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
# try:
browser.get(link)

input1 = browser.find_element_by_name("first_name").send_keys("Ivan")
input2 = browser.find_element_by_name("last_name").send_keys("Petrov")
input3 = browser.find_element_by_class_name("city").send_keys("Smolensk")
input4 = browser.find_element_by_id("country").send_keys("Russia")
button = browser.find_element_by_css_selector("button.btn")
button.click()
# finally:
#     browser.quit()