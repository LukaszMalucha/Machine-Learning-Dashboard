from selenium.webdriver.common.by import By

from tests.acceptance.locators.edit_template_page import EditTemplatePageLocators
from tests.acceptance.page_model.base_page import BasePage


class EditTemplatePage(BasePage):
    @property
    def url(self):
        return super(EditTemplatePage, self).url + '/edit_code/1'

    @property
    def form(self):
        return self.driver.find_element(*EditTemplatePageLocators.FORM_EDIT_CODE)

    @property
    def submit_button(self):
        return self.driver.find_element(*EditTemplatePageLocators.SUBMIT_BUTTON)


    def form_field(self, name):
        return self.form.find_element(By.NAME, name)
