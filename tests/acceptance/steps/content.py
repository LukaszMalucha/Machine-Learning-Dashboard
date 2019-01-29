from behave import *

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


@then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed()


@then('The title tag has content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.driver)
    assert page.title.text == content


@then('There are all questions shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    questions = [question for question in page.question]
    assert len(questions) == 5


@then('I can see there is a table on the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.table.is_displayed()

@then('I can see there are Github Repos in the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.github_repos.is_displayed()


@then('I can see there is a signup form on the page')
def step_impl(context):
    page = SignupPage(context.driver)
    assert page.form.is_displayed()


@then('I can see there is a login form on the page')
def step_impl(context):
    page = LoginPage(context.driver)
    assert page.form.is_displayed()


@then('I can see there is an add template form on the page')
def step_impl(context):
    page = AddTemplatePage(context.driver)
    assert page.form.is_displayed()

@then('I can see there is an edit template form on the page')
def step_impl(context):
    page = EditTemplatePage(context.driver)
    assert page.form.is_displayed()


@then('I can see there four forms displayed on the page')
def step_impl(context):
    page = ManagedbPage(context.driver)
    assert page.add_algorithm_type_form.is_displayed()
    assert page.add_complexity_form.is_displayed()
    assert page.add_method_form.is_displayed()
    assert page.add_algorithm_form.is_displayed()

@then('I can see there are three classification algorithm choices')
def step_impl(context):
    page = ClassificationPage(context.driver)
    assert len(page.navigation) == 3

@then('I can see there are two clustering algorithm choices')
def step_impl(context):
    page = ClusteringPage(context.driver)
    assert len(page.navigation) == 2

@then('I can see there are three regression algorithm choices')
def step_impl(context):
    page = RegressionPage(context.driver)
    assert len(page.navigation) == 3

@then('The answer is "Suggested Machine Learning algorithms are: Naive Bayes & LinearSVC"')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.answer.text == "Suggested Machine Learning algorithms are: Naive Bayes & LinearSVC"

@then('I can see there is a plot on the page')
def step_impl(context):
    page = ClassificationPage(context.driver)
    assert page.plot.is_displayed()


