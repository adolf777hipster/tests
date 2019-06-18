import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

num1 = browser.find_element_by_id('num1').text
num2 = browser.find_element_by_id('num2').text

summa = int(num1)+int(num2)


select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(summa))

browser.find_element_by_css_selector("[type = 'submit']").click()
