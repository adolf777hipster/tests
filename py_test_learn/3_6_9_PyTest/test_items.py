import time
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_add_to_trash(browser):
    browser.get(link)
    time.sleep(2)
    browser.find_element_by_id("add_to_basket_form").click()
    result = browser.find_element_by_class_name('alertinner').text
    if result == "Coders at Work has been added to your basket.":
        print("You  entered English language with command string -->  pytest --language=es test_items.py ")
    elif result == "Coders at Work a été ajouté à votre panier.":
        print("You  entered FRENCH language with command string -->   pytest --language=fr test_items.py ")
    else:
        print(
            "Sorry, but You  entered incorrect language check out your command for start test they must be:"
            "\npytest --language=es test_items.py for ENGLISH"
            "\npytest --language=fr test_items.py for FRENCH")
