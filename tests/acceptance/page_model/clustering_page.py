from tests.acceptance.locators.clustering_page import ClusteringPageLocators
from tests.acceptance.page_model.base_page import BasePage


class ClusteringPage(BasePage):
    @property
    def url(self):
        return super(ClusteringPage, self).url + '/clustering'

    @property
    def plot_determine_section(self):
        return self.driver.find_element(*ClusteringPageLocators.PLOT_DETERMINE)

    @property
    def plot_section(self):
        return self.driver.find_element(*ClusteringPageLocators.PLOT)

    @property
    def accuracy_section(self):
        return self.driver.find_element(*ClusteringPageLocators.ACCURACY)

    @property
    def navigation(self):
        return self.driver.find_elements(*ClusteringPageLocators.NAV_LINKS)
