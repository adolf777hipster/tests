# 3.6 (3)
import math
import time

import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\n Start browser and test!")
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    yield browser
    print("\n Test successful and quit browser!")
    browser.quit()


@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    answer = math.log(int(time.time()))
    print("\n Ответ на данное задание - {}".format(answer))
    browser.find_element_by_css_selector("[placeholder='Type your answer here...']").send_keys(str(answer))
    browser.find_element_by_class_name("submit-submission").click()
    expected_text = browser.find_element_by_class_name('smart-hints__hint').text
    assert expected_text == "Correct!"
