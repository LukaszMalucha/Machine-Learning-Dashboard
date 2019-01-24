from selenium.webdriver.common.by import By

from tests.acceptance.locators.add_template_page import AddTemplatePageLocators
from tests.acceptance.page_model.base_page import BasePage


class AddTemplatePage(BasePage):
    @property
    def url(self):
        return super(AddTemplatePage, self).url + '/add_request'

    @property
    def form(self):
        return self.driver.find_element(*AddTemplatePageLocators.FORM_NEW_CODE)

    @property
    def submit_button(self):
        return self.driver.find_element(*AddTemplatePageLocators.SUBMIT_BUTTON)

    @property
    def dropdowns(self):
        return self.driver.find_elements(*AddTemplatePageLocators.DROPDOWN)


    def form_field(self, name):
        return self.form.find_element(By.NAME, name)


