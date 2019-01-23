from tests.acceptance.locators.classification_page import ClassificationPageLocators
from tests.acceptance.page_model.base_page import BasePage


class ClassificationPage(BasePage):
    @property
    def url(self):
        return super(ClassificationPage, self).url + '/classification'

    @property
    def plot(self):
        return self.driver.find_element(*ClassificationPageLocators.PLOT)

    @property
    def accuracy_section(self):
        return self.driver.find_element(*ClassificationPageLocators.ACCURACY)

    @property
    def navigation(self):
        return self.driver.find_elements(*ClassificationPageLocators.NAV_LINKS)




