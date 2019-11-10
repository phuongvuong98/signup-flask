from behave import *


@then('I click login twitter')
def step_impl(context):
    context.browser.find_element_by_id('submitTw').click()
    context.browser.switch_to_window("windowtw")
    email = context.browser.find_element_by_id('username_or_email')
    email.send_keys('phuongvuong98')
    password = context.browser.find_element_by_id('password')
    password.send_keys('Vuong0935986100')
    context.browser.find_element_by_id('allow').click()



@then('I have already signed up twitter.')
def step_impl(context):
    result = context.browser.find_element_by_id('result')
    assert "signed up twitter" in result.text
