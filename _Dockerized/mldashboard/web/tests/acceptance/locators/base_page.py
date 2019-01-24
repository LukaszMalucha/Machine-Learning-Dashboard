from selenium.webdriver.common.by import By


class BasePageLocators:
    TITLE = By.TAG_NAME, 'strong'
    NAV_LINKS =  By.ID, 'navigation'
    DROPDOWN = By.ID, 'user_dropdown'
    DROPDOWN_LINKS = By.ID, 'dropdown_link'
    PAGE = By.ID, 'page-index'
    TABLE = By.CLASS_NAME, 'table-responsive'
    GITHUB_USER = By.ID, 'gh-username'
    GITHUB_REPOS = By.ID, 'repo_content'
