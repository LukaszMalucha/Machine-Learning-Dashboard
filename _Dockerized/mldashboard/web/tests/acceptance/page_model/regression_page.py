from tests.acceptance.locators.regression_page import RegressionPageLocators
from tests.acceptance.page_model.base_page import BasePage


class RegressionPage(BasePage):
    @property
    def url(self):
        return super(RegressionPage, self).url + '/regression'

    @property
    def plot_section(self):
        return self.driver.find_element(*RegressionPageLocators.PLOT)

    @property
    def accuracy_section(self):
        return self.driver.find_element(*RegressionPageLocators.ACCURACY)

    @property
    def navigation(self):
        return self.driver.find_elements(*RegressionPageLocators.NAV_LINKS)




