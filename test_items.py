#####test_items.py#####

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestMainPage:

    def test_of_page(self, browser, request):

        lang = request.config.getoption("language")
        link = f"http://selenium1py.pythonanywhere.com/{lang}/catalogue/coders-at-work_207/"
        browser.get(link)

        #   Cделал таким образом, так как elements возвращают пустой список,
        #   если кнопка не найдена а [] = false для ассерт.
        #   если искать кнопку через WebDriverWait то при неудачи тест падает с TimeoutException,
        #   не доходя до assert

        but = browser.find_elements(By.CSS_SELECTOR, "button.btn-primary.btn-add-to-basket")

        assert but, "ERROR, button has not been found"