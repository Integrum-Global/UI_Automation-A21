###
 # Login steps 
 #
###

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xpaths

@given('I am on the login page of a21-dev web application')
def step_impl(context):
    context.browser.get(context.base_url)
    #wait for the login page to load
    WebDriverWait(context.browser, 5).until(EC.presence_of_element_located((By.NAME, "email")))

@when('I enter the username as "{user_name}" and password "{password}"')
def step_impl(context, user_name, password):
    #enter the username and password
    e_username = context.browser.find_element(By.NAME, "email")
    e_username.send_keys(user_name)
    e_username.send_keys(Keys.TAB)
    #enter the password
    e_password = context.browser.find_element(By.XPATH, xpaths.LOGIN_PASSWORD)
    e_password.send_keys(password)
    #click on the login button
    e_login_button = context.browser.find_element(By.XPATH, xpaths.LOGIN_BUTTON)
    e_login_button.click()

@then('I should be able to login into the application')
def step_impl(context):
    #wait for the login to complete
    WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.XPATH, xpaths.LANDING_PAGE_HEADER)))
    #verify the login by checking the header
    header = context.browser.find_element(By.XPATH, xpaths.LANDING_PAGE_HEADER)
    assert header.text == "Plan Management"
    #logout for new tests
    profile = context.browser.find_element(By.XPATH, xpaths.LANDING_PAGE_PROFILE)
    profile.click()
    context.browser.implicitly_wait(5)
    logout = context.browser.find_element(By.XPATH, xpaths.LANDING_PAGE_LOGOUT)
    logout.click()

@then('I should see error message')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.XPATH, xpaths.LOGIN_ERROR_MESSAGE)))
    error_message = context.browser.find_element(By.XPATH, xpaths.LOGIN_ERROR_MESSAGE)
    assert error_message.text == "Sorry"



