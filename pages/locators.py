from selenium.webdriver.common.by import By


class MainPageLocators:
    LOG_IN_BUTTON = (By.CLASS_NAME, 'nav.navbar-nav.navbar-right')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
