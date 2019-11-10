from behave import *


@then('I click login facebook')
def step_impl(context):
    context.browser.find_element_by_id('submitFb').click()
    context.browser.switch_to_window("windowfb")
    email = context.browser.find_element_by_id('email')
    email.send_keys('phuongvuong98@gmail.com')
    password = context.browser.find_element_by_id('pass')
    password.send_keys('Vuong0935986100')
    context.browser.find_element_by_id('loginbutton').click()


@then('I have already signed up facebook.')
def step_impl(context):
    result = context.browser.find_element_by_id('result')
    assert "signed up facebook" in result.text


@then('You sign up successful')
def step_impl(context):
    result = context.browser.find_element_by_id('result')
    assert "successful" in result.text
