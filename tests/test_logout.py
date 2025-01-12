from locators import TestLocators
from conftest import driver, correct_login
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

class TestLogout:

    # Выход из личного кабинета
    def test_logout_from_personal_account(self, driver, correct_login):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_make_order))
        driver.find_element(*TestLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_logout))
        driver.find_element(*TestLocators.button_logout).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_login))
        assert driver.find_element(*TestLocators.button_login).is_enabled()
