from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(5)
    assert browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button")