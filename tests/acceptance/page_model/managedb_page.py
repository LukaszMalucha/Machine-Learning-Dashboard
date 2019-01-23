from selenium.webdriver.common.by import By

from tests.acceptance.locators.managedb_page import ManagedbPageLocators
from tests.acceptance.page_model.base_page import BasePage


class ManagedbPage(BasePage):
    @property
    def url(self):
        return super(ManagedbPage, self).url + '/manage_db'

    @property
    def add_algorithm_type_form(self):
        return self.driver.find_element(*ManagedbPageLocators.ADD_ALGORTIHM_TYPE_FORM)

    @property
    def submit_algorithm_type(self):
        return self.driver.find_element(*ManagedbPageLocators.SUBMIT_ALGORITHM_TYPE)

    def add_algorithm_type_form_field(self, name):
        return self.add_algorithm_type_form.find_element(By.NAME, name)

    @property
    def add_complexity_form(self):
        return self.driver.find_element(*ManagedbPageLocators.ADD_COMPLEXITY_FORM)

    @property
    def submit_complexity(self):
        return self.driver.find_element(*ManagedbPageLocators.SUBMIT_COMPLEXITY)

    def add_complexity_form_field(self, name):
        return self.add_complexity_form_field.find_element(By.NAME, name)

    @property
    def add_method_form(self):
        return self.driver.find_element(*ManagedbPageLocators.ADD_METHOD_FORM)

    @property
    def submit_method(self):
        return self.driver.find_element(*ManagedbPageLocators.SUBMIT_METHOD)

    def add_method_form_field(self, name):
        return self.add_algorithm_type_form.find_element(By.NAME, name)

    @property
    def add_algorithm_form(self):
        return self.driver.find_element(*ManagedbPageLocators.ADD_ALGORITHM_FORM)

    @property
    def submit_algorithm(self):
        return self.driver.find_element(*ManagedbPageLocators.SUBMIT_ALGORITHM)

    def add_algorithm_form_field(self, name):
        return self.add_algorithm_form.find_element(By.NAME, name)
