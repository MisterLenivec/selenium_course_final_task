import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: 'en', 'ru' or other")


def chrome_options(user_language):
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language}
    )
    return options


def firefox_oprions(user_language):
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", user_language)
    return fp


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(
            options=chrome_options(user_language)
        )
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(
            firefox_profile=firefox_oprions(user_language)
        )
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()
