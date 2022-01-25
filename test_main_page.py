import time

from selenium.webdriver.common.by import By

from .pages.locators import MainPageLocators
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


def go_to_login_page(browser):
    login_link = browser.find_element(*MainPageLocators.LOG_IN_BUTTON)
    login_link.click()


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

    page2 = LoginPage(browser, link)
    page2.should_be_login_url()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def should_be_login_link(self):
    assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"





