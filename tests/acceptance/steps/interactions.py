from behave import *

from tests.acceptance.page_model.add_template_page import AddTemplatePage
from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.classification_page import ClassificationPage
from tests.acceptance.page_model.login_page import LoginPage
from tests.acceptance.page_model.signup_page import SignupPage

use_step_matcher('re')


@when('I click on the "(.*)" link')
def step_impl(context, link_text):
    page = BasePage(context.driver)
    links = page.navigation

    matching_links = [l for l in links if l.text == link_text]
    matching_links[0].click()
    # if len(matching_links) > 0:
    #     matching_links[0].click()
    # else:
    #     raise RuntimeError()


@when('I click on the "(.*)" dropdown link')
def step_impl(context, link_text):
    page = BasePage(context.driver)
    links = page.dropdown_links
    matching_links = [l for l in links if l.text == link_text]
    matching_links[0].click()


@when('I click on the dropdown menu')
def step_impl(context):
    page = BasePage(context.driver)
    page.dropdown.click()


@when('I enter "(.*)" in the "(.*)" field')
def step_impl(context, content, field_name):
    page = SignupPage(context.driver)
    page.form_field(field_name).send_keys(content)


@when('I enter "(.*)" in the "(.*)" login field')
def step_impl(context, content, field_name):
    page = LoginPage(context.driver)
    page.form_field(field_name).send_keys(content)


@when('I enter "(.*)" in the "(.*)" add template form field')
def step_impl(context, content, field_name):
    page = AddTemplatePage(context.driver)
    page.form_field(field_name).send_keys(content)


@when('I click on the "(.*)" navigation link')
def step_impl(context, link_text):
    page = ClassificationPage(context.driver)
    links = page.navigation
    matching_links = [l for l in links if l.text == link_text]
    matching_links[0].click()


@when('I scroll to the bottom of the page')
def step_impl(context):
    page = ClassificationPage(context.driver)
    page.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")



@when('I choose "(.*)" field')
def step_impl(context, field_name):
    page = BasePage(context.driver)
    page.form_field(field_name).click()


@when('I press the submit button')
def step_impl(context):
    page = SignupPage(context.driver)
    page.submit_button.click()


@when('I press the login button')
def step_impl(context):
    page = LoginPage(context.driver)
    page.submit_button.click()



