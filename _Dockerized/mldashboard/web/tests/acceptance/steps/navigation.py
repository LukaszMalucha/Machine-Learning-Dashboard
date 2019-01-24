from behave import *
from selenium import webdriver

from tests.acceptance.page_model.add_template_page import AddTemplatePage
from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.classification_page import ClassificationPage
from tests.acceptance.page_model.clustering_page import ClusteringPage
from tests.acceptance.page_model.edit_template_page import EditTemplatePage
from tests.acceptance.page_model.login_page import LoginPage
from tests.acceptance.page_model.managedb_page import ManagedbPage
from tests.acceptance.page_model.regression_page import RegressionPage
from tests.acceptance.page_model.signup_page import SignupPage

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')  ## path to chromedriver
    page = BasePage(context.driver)
    context.driver.get(page.url)


@given('I am on the signup page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')
    page = SignupPage(context.driver)
    context.driver.get(page.url)


@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')
    page = LoginPage(context.driver)
    context.driver.get(page.url)


@given('I am on the add template page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')
    page = AddTemplatePage(context.driver)
    context.driver.get(page.url)


@given('I am on the edit template page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')
    page = EditTemplatePage(context.driver)
    context.driver.get(page.url)


@given('I am on the manage db page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')
    page = ManagedbPage(context.driver)
    context.driver.get(page.url)


@given('I am on the classification page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')
    page = ClassificationPage(context.driver)
    context.driver.get(page.url)


@given('I am on the clustering page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')
    page = ClusteringPage(context.driver)
    context.driver.get(page.url)


@given('I am on the regression page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')
    page = RegressionPage(context.driver)
    context.driver.get(page.url)


@then('I am on the homepage')
def step_impl(context):
    expected_url = BasePage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the signup page')
def step_impl(context):
    expected_url = SignupPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the login page')
def step_impl(context):
    expected_url = LoginPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the manage db page')
def step_impl(context):
    expected_url = ManagedbPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the add template page')
def step_impl(context):
    expected_url = AddTemplatePage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the edit template page')
def step_impl(context):
    expected_url = EditTemplatePage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the classification page')
def step_impl(context):
    expected_url = ClassificationPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the clustering page')
def step_impl(context):
    expected_url = ClusteringPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the regression page')
def step_impl(context):
    expected_url = RegressionPage(context.driver).url
    assert context.driver.current_url == expected_url

@then('I am on the library page')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/'
    assert context.driver.current_url == expected_url