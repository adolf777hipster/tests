import time
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_add_to_trash(browser):
    browser.get(link)
    # time.sleep(30)
    browser.find_element_by_id("add_to_basket_form").click()
