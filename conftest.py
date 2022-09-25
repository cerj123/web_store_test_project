import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


list_langs = ["es", "ru", "fr", "en"]


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose user language from the list: " + str(list_langs))


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    if language in list_langs:
        print(f"\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be from the list " + str(list_langs))

    yield browser
    print("\nquit browser..")
    browser.quit()
