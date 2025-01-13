from locators import TestLocators
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import generation_random_name
import generation_random_email
import generation_random_password
import pytest

class TestRegistration:

    # Регистрация с валидными данными

    def test_registration_success(self, driver):
        random_name = generation_random_name.random_value
        random_email = generation_random_email.random_email
        random_password = generation_random_password.random_password
        driver.find_element(*TestLocators.button_login_main_page).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_register))
        driver.find_element(*TestLocators.button_register).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_submit_register))
        driver.find_element(*TestLocators.name).send_keys(random_name)
        driver.find_element(*TestLocators.email).send_keys(random_email)
        driver.find_element(*TestLocators.password).send_keys(random_password)
        driver.find_element(*TestLocators.button_submit_register).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_login))
        assert driver.find_element(*TestLocators.button_recovery_password).is_enabled()


    # Регистрация с пустым полем "Имя"
    def test_registration_empty_name_input(self, driver):
        random_email = generation_random_email.random_email
        random_password = generation_random_password.random_password
        driver.find_element(*TestLocators.button_login_main_page).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_register))
        driver.find_element(*TestLocators.button_register).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_submit_register))
        driver.find_element(*TestLocators.name).send_keys('')
        driver.find_element(*TestLocators.email).send_keys(random_email)
        driver.find_element(*TestLocators.password).send_keys(random_password)
        driver.find_element(*TestLocators.button_submit_register).click()
        WebDriverWait(driver, 3).until(expected_conditions.invisibility_of_element(TestLocators.button_recovery_password))
        assert driver.find_element(*TestLocators.button_submit_register).is_enabled()


    # Регистрация с невалидной почтой
    def test_registration_invalid_email(self, driver):
        random_name = generation_random_name.random_value
        random_password = generation_random_password.random_password
        driver.find_element(*TestLocators.button_login_main_page).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_register))
        driver.find_element(*TestLocators.button_register).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_submit_register))
        driver.find_element(*TestLocators.name).send_keys(random_name)
        driver.find_element(*TestLocators.email).send_keys('nikitayandexgmail.com')
        driver.find_element(*TestLocators.password).send_keys(random_password)
        driver.find_element(*TestLocators.button_submit_register).click()
        WebDriverWait(driver, 3).until(expected_conditions.invisibility_of_element(TestLocators.button_recovery_password))
        assert driver.find_element(*TestLocators.button_submit_register).is_enabled()


    # Проверка регистрации с символами миньше 6 в пароле + проверка текста ошибки
    @pytest.mark.parametrize('invalid', ['n', 'nk', 'nko', 'nkop', 'nkopy'])
    def test_registration_invalid_password(self, driver, invalid):
        random_name = generation_random_name.random_value
        random_email = generation_random_email.random_email
        driver.find_element(*TestLocators.button_login_main_page).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_register))
        driver.find_element(*TestLocators.button_register).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_submit_register))
        driver.find_element(*TestLocators.name).send_keys(random_name)
        driver.find_element(*TestLocators.email).send_keys(random_email)
        driver.find_element(*TestLocators.password).send_keys(invalid)
        driver.find_element(*TestLocators.button_submit_register).click()
        WebDriverWait(driver, 3).until(expected_conditions.invisibility_of_element(TestLocators.button_recovery_password))
        assert driver.find_element(*TestLocators.notification_password).text == 'Некорректный пароль'


    # Проверка регистрации с пустым паролем
    def test_registration_empty_password(self, driver):
        random_email = generation_random_email.random_email
        random_name = generation_random_name.random_value
        driver.find_element(*TestLocators.button_login_main_page).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_register))
        driver.find_element(*TestLocators.button_register).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_submit_register))
        driver.find_element(*TestLocators.name).send_keys(random_name)
        driver.find_element(*TestLocators.email).send_keys(random_email)
        driver.find_element(*TestLocators.password).send_keys('')
        driver.find_element(*TestLocators.button_submit_register).click()
        WebDriverWait(driver, 3).until(expected_conditions.invisibility_of_element(TestLocators.button_recovery_password))
        assert driver.find_element(*TestLocators.button_submit_register).is_enabled()
