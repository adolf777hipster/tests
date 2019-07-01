import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: es or fr")


# For Chrome
@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("language")
    if language_name == "es":
        print('\nStart browser with English language')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': "en"})
        browser = webdriver.Chrome(options=options)

    elif language_name == "fr":
        print('\nStart browser with French language')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': "fr"})
        browser = webdriver.Chrome(options=options)
    else:
        print("Language {} still is not implemented".format(language_name))
    browser.implicitly_wait(1)
    yield browser
    print("\nQuit browser!")
    browser.quit()
