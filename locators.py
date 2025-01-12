from selenium.webdriver.common.by import By

class TestLocators:
    name = By.XPATH, '//label[text()="Имя"]/following-sibling::input' # Поле "Имя"
    email = By.XPATH, '//label[text()="Email"]/following-sibling::input' # Поле "Пароль"
    password = By.NAME, 'Пароль' # Поле "Пароль"
    button_register = By.XPATH, '//a[text() = "Зарегистрироваться"]' # Кнопка перехода на форму регистрации
    button_login_from_registration = By.XPATH, '//a[text() = "Войти"]' # Кнопка "Войти" на форме регистрации
    notification_password = By.XPATH, '//p[text() = "Некорректный пароль"]' # Текст ошибки при вводе невалидного пароля
    email_auth = By.XPATH, '//label[text()="Email"]/following-sibling::input' # Поле почты для авторизации
    password_auth = By.XPATH, '//input[@name = "Пароль"]' # Поле пароля для авторизации
    button_login = By.XPATH, '//button[text()="Войти"]' # Кнопка "Войти"
    button_submit_register = By.XPATH, '//button[text() = "Зарегистрироваться"]' # Кнопка подтверждения регистрации
    button_recovery_password = By.XPATH, '//a[text() = "Восстановить пароль"]' # Кнопка восстановления пароля
    button_login_password_recovery_form = By.XPATH, '//a[text() = "Войти"]' # Кнопка "Войти" из формы восстановления пароля
    button_logout = By.XPATH, '//button[@type = "button"]' # Кнопка "Выйти"
    button_login_main_page = By.XPATH, './/button[text() = "Войти в аккаунт"]' # Кнопка "Войти в аккаунт" на главной странице
    button_personal_account = By.XPATH, '//p[text() = "Личный Кабинет"]' # Кнопка "Личный Кабинет"
    button_make_order = By.XPATH, '//button[text()="Оформить заказ"]' # Кнопка "Оформить заказ"
    button_constructor_header = By.XPATH, '//p[text() = "Конструктор"]' # Кнопка "Конструктор"
    active_section = By.XPATH, ('//div[@class = "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]') # Селектор выделенного раздела в конструкторе
    buns_section = By.XPATH, '//span[text() = "Булки"]' # Раздел "Булки"
    sauces_section = By.XPATH, '//span[text() = "Соусы"]' # Раздел "Соусы"
    toppings_section = By.XPATH, '//span[text() = "Начинки"]' # Раздел "Начинки"
    logo_header = By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]' # Лого в шапке
    notification_account = By.XPATH, '//nav//p[text() = "В этом разделе вы можете изменить свои персональные данные"]' # Сообщение вличном кабинете
    field_name_in_personal_account = By.NAME, 'Name' # Поле "Имя" в личном кабинете