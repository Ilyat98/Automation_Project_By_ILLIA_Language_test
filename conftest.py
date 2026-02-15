import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox


#Использую котеж для дальнешо разширения списка допустимых параметров
list_of_languages = ("ru", "es", "uk")
list_of_browsers = ("chrome", "firefox")


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default="ru",
                     help="Pls, choose language: ru, es, or uk")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")

    #проверка на правильность ввода языка и браузера
    if language not in list_of_languages:
        raise pytest.UsageError(
            f"--language must be one of {list_of_languages}")

    if browser_name not in list_of_browsers:
        raise pytest.UsageError(
            f"--browser_name  must be one of {list_of_browsers}")


    #Тут оставил таким образом, так как для хрома и мозиллы немного разные параметры используют.
    # Позже подумаю как унифицировать
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options_firefox = OptionsFirefox()
        options_firefox.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()