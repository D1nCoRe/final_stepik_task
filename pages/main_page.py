import time
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        log_in_button = self.browser.find_element(*MainPageLocators.LOG_IN_BUTTON)
        log_in_button.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOG_IN_BUTTON), "Login link is not presented"
