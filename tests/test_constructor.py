from locators import TestLocators
from conftest import driver, correct_login
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class TestConstructor:

    # Проверка перехода к разделу "Соусы" из "Булок"
    def test_checkout_to_sauces_from_buns(self, driver, correct_login):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_make_order))
        driver.find_element(*TestLocators.sauces_section).click()
        assert driver.find_element(*TestLocators.active_section).text == 'Соусы'


    # Проверка перехода к разделу "Начинки" из "Булок"
    def test_checkout_to_toppings_from_buns(self, driver, correct_login):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_make_order))
        driver.find_element(*TestLocators.toppings_section).click()
        assert driver.find_element(*TestLocators.active_section).text == 'Начинки'


    # Проверка перехода к разделу "Булки" из "Соусов"
    def test_checkout_to_buns_from_sauces(self, driver, correct_login):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_make_order))
        driver.find_element(*TestLocators.sauces_section).click()
        assert driver.find_element(*TestLocators.active_section).text == 'Соусы'
        driver.find_element(*TestLocators.buns_section).click()
        assert driver.find_element(*TestLocators.active_section).text == 'Булки'


    # Проверка перехода к разделу "Начинки" из "Соусов"
    def test_checkout_to_toppings_from_sauces(self, driver, correct_login):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_make_order))
        driver.find_element(*TestLocators.sauces_section).click()
        assert driver.find_element(*TestLocators.active_section).text == 'Соусы'
        driver.find_element(*TestLocators.toppings_section).click()
        assert driver.find_element(*TestLocators.active_section).text == 'Начинки'


    # Проверка перехода к разделу "Булки" из "Начинок"
    def test_checkout_to_buns_from_toppings(self, driver, correct_login):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_make_order))
        driver.find_element(*TestLocators.toppings_section).click()
        assert driver.find_element(*TestLocators.active_section).text == 'Начинки'
        driver.find_element(*TestLocators.buns_section).click()
        assert driver.find_element(*TestLocators.active_section).text == 'Булки'


    # Проверка перехода к разделу "Соусы" из "Начинок"
    def test_checkout_to_sauces_from_toppings(self, driver, correct_login):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_make_order))
        driver.find_element(*TestLocators.toppings_section).click()
        assert driver.find_element(*TestLocators.active_section).text == 'Начинки'
        driver.find_element(*TestLocators.sauces_section).click()
        assert driver.find_element(*TestLocators.active_section).text == 'Соусы'