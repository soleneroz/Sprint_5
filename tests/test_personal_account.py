from locators import TestLocators
from conftest import driver, correct_login
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from user_data import UserData

class TestPersonalAccount:

    # Проверка перехода в личный кабинет
    def test_checkout_to_personal_account_from_main_page(self, driver, correct_login):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_make_order))
        driver.find_element(*TestLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_logout))
        assert driver.find_element(*TestLocators.notification_account).is_displayed()
        assert driver.find_element(*TestLocators.field_name_in_personal_account).get_attribute('value') == UserData.username
