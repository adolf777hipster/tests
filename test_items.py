link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_basket_button_should_be_present(browser):
    browser.get(link)
    browser.find_element_by_css_selector(".btn-add-to-basket")