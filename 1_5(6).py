from selenium import webdriver

link = "http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_name('first_name').send_keys("Ivan")

input2 = browser.find_element_by_name('last_name').send_keys("Petrov")

input3 = browser.find_element_by_class_name('city').send_keys("Smolensk")

input4 = browser.find_element_by_css_selector('input#country.form-control').send_keys("Russia")

button = browser.find_element_by_xpath('//div//*[@type = "submit"]')
button.click()
