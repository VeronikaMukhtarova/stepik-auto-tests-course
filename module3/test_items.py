import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_basket_button(browser):
    browser.get(link)
    time.sleep(5)
    basket_button_available = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert basket_button_available, "Кнопка Добавить в корзину не найдена"