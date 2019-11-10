from behave import *


@given('I open website')
def step_impl(context):
    context.browser.get("https://dcb8d6c5.ngrok.io/register")


@then('I print the html')
def step_impl(context):
    title = context.browser.find_element_by_tag_name('h1')
    assert "Register" in title.text


@then('I input email')
def step_impl(context):
    email = context.browser.find_element_by_id('email')
    email.send_keys('vuong1@gmail.com')


@then('I input incorrect email')
def step_impl(context):
    email = context.browser.find_element_by_id('email')
    email.send_keys('vuong1@1111')


@then('I input password')
def step_impl(context):
    password = context.browser.find_element_by_id('password')
    password.send_keys('huhu')


@then('I submit form')
def step_impl(context):
    submit = context.browser.find_element_by_id('submit')
    submit.click()


@then('I print email error')
def step_impl(context):
    error = context.browser.find_elements_by_class_name('error')[0]
    assert "This field is required." in error.text


@then('I print incorrect email error')
def step_impl(context):
    error = context.browser.find_elements_by_class_name('error')[0]
    assert "Invalid email address." in error.text


@then('I print password error')
def step_impl(context):
    error = context.browser.find_elements_by_class_name('error')[1]
    assert "This field is required." in error.text
