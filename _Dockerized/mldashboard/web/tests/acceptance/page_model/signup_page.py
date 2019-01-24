from selenium.webdriver.common.by import By

from tests.acceptance.locators.signup_page import SignupPageLocators
from tests.acceptance.page_model.base_page import BasePage


class SignupPage(BasePage):
    @property
    def url(self):
        return super(SignupPage, self).url + '/signup'

    @property
    def form(self):
        return self.driver.find_element(*SignupPageLocators.SIGNUP_FORM)

    @property
    def submit_button(self):
        return self.driver.find_element(*SignupPageLocators.SUBMIT_BUTTON)

    def form_field(self, name):
        return self.form.find_element(By.NAME, name)
