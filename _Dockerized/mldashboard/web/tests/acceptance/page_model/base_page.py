from tests.acceptance.locators.base_page import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'http://127.0.0.1:5000'

    @property
    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE)

    @property
    def navigation(self):
        return self.driver.find_elements(*BasePageLocators.NAV_LINKS)

    @property
    def dropdown(self):
        return self.driver.find_element(*BasePageLocators.DROPDOWN)

    @property
    def dropdown_links(self):
        return self.driver.find_elements(*BasePageLocators.DROPDOWN_LINKS)

    @property
    def table(self):
        return self.driver.find_element(*BasePageLocators.TABLE)

    @property
    def github_user(self):
        return self.driver.find_element(*BasePageLocators.GITHUB_USER)

    @property
    def github_repos(self):
        return self.driver.find_element(*BasePageLocators.GITHUB_REPOS)
