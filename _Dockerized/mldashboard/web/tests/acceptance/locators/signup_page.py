from selenium.webdriver.common.by import By


class SignupPageLocators:
    SIGNUP_FORM = By.ID, 'signup-form'
    USERNAME_FIELD = By.ID, 'username'
    EMAIL_FIELD = By.ID, 'email'
    PASSWORD = By.ID, 'password'
    SUBMIT_BUTTON = By.ID, 'submit-button'
