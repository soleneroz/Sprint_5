import pytest
from selenium import webdriver
from locators import TestLocators
from user_data import UserData

# Подключение webdriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

# Авторизация корректными данными
@pytest.fixture
def correct_login(driver):
    driver.find_element(*TestLocators.button_login_main_page).click()
    driver.find_element(*TestLocators.email_auth).send_keys(UserData.email)
    driver.find_element(*TestLocators.password_auth).send_keys(UserData.password)
    driver.find_element(*TestLocators.button_login).click()