##
# Define the environments for the tests
#
##

from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from steps.xpaths import LOGIN_PASSWORD, LOGIN_BUTTON    
import time

@fixture
def setup_chrome(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    context.browser = webdriver.Chrome()
    yield context.browser
    context.browser.quit()

def before_all(context):
    use_fixture(setup_chrome, context)
    context.base_url = "https://a21-dev.integrum.global"
    context.browser.maximize_window()

def after_all(context):
    context.browser.quit()
  

def before_feature (context,feature):
    print("Before feature\n")
    if feature.name == "Login into integrum mobility":
        return 
    ## Login into the application
    context.browser.get(context.base_url)
    time.sleep(2)
    
    #wait for the login page to load
    WebDriverWait(context.browser, 5).until(EC.presence_of_element_located((By.NAME, "email")))
    e_username = context.browser.find_element(By.NAME, "email")
    e_username.send_keys("parimal.nakrani@integrum.global")
    e_username.send_keys(Keys.TAB)
    #enter the password
    e_password = context.browser.find_element(By.XPATH, LOGIN_PASSWORD)
    e_password.send_keys("123456")
    #click on the login button
    e_login_button = context.browser.find_element(By.XPATH, LOGIN_BUTTON)
    e_login_button.click()
    time.sleep(5) 
    context.browser.implicitly_wait(5)



# implement logout.
#def after_feature (context):
     #print("After feature\n")
      #context.browser.get(context,'https://boonrawd-dev.integrum.global/pre-mission/assetType')
      #context.browser.implicitly_wait(5)

     
