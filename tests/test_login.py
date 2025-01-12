from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from conftest import driver
from user_data import UserData

class TestLogin:
    # Проверка авторизации с главной страницы
    def test_login_from_main_page(self, driver):
        driver.find_element(*TestLocators.button_login_main_page).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_register))
        driver.find_element(*TestLocators.email_auth).send_keys(UserData.email)
        driver.find_element(*TestLocators.password_auth).send_keys(UserData.password)
        driver.find_element(*TestLocators.button_login).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_make_order))
        assert driver.find_element(*TestLocators.button_make_order).is_enabled()


    # Проверка авторизации по кнопке из Личного кабинета
    def test_login_from_button_personal_account(self, driver):
        driver.find_element(*TestLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_register))
        driver.find_element(*TestLocators.email_auth).send_keys(UserData.email)
        driver.find_element(*TestLocators.password_auth).send_keys(UserData.password)
        driver.find_element(*TestLocators.button_login).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_make_order))
        assert driver.find_element(*TestLocators.button_make_order).is_enabled()


    # Проверка авторизации из формы регистрации
    def test_login_from_registration_form(self, driver):
        driver.find_element(*TestLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_register))
        driver.find_element(*TestLocators.button_register).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_login_from_registration))
        driver.find_element(*TestLocators.button_login_from_registration).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_register))
        driver.find_element(*TestLocators.email_auth).send_keys(UserData.email)
        driver.find_element(*TestLocators.password_auth).send_keys(UserData.password)
        driver.find_element(*TestLocators.button_login).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_make_order))
        assert driver.find_element(*TestLocators.button_make_order).is_enabled()


    # Проверка авторизации через форму восстановления пароля
    def test_login_from_recovery_password_form(self, driver):
        driver.find_element(*TestLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_recovery_password))
        driver.find_element(*TestLocators.button_recovery_password).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_login_password_recovery_form))
        driver.find_element(*TestLocators.button_login_password_recovery_form).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_register))
        driver.find_element(*TestLocators.email_auth).send_keys(UserData.email)
        driver.find_element(*TestLocators.password_auth).send_keys(UserData.password)
        driver.find_element(*TestLocators.button_login).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_make_order))
        assert driver.find_element(*TestLocators.button_make_order).is_enabled()
