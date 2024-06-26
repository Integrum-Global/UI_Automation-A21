from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
import time, xpaths


@given('I am on the Skillset Page of a21-dev web application')
def step_impl(context):
    context.browser.get('https://a21-dev.integrum.global/pre-mission/skillset')
    time.sleep(1)

#Check Total Visibility Column:
    
@when('User clicks on the Total visibility column to unchecks/checks the visibility status of the skillset')
def enter_value(context):

    #User click Total visibility column
    visibility_column_button =context.browser.find_element(By.XPATH,xpaths.SKILLSET_VISIBILITY_COLUMN_BTN) 
    visibility_column_button.click()
    time.sleep(1)

    #Unchecks the No
    unchecks_no=context.browser.find_element(By.XPATH,xpaths.SKILLSET_UNCHECKS_NO)
    unchecks_no.click()
    time.sleep(1)

    #Unchecks the Name
    unchecks_name=context.browser.find_element(By.XPATH,xpaths.SKILLSET_UNCHECKS_NAME)
    unchecks_name.click()
    time.sleep(1)
    
    #Unchecks the Category
    unchecks_category=context.browser.find_element(By.XPATH,xpaths.SKILLSET_UNCHECKS_CATEGORY)
    unchecks_category.click()
    time.sleep(1)

    #Unchecks the Subcategory
    unchecks_subcategory=context.browser.find_element(By.XPATH,xpaths.SKILLSET_UNCHECKS_SUBCATEGORY)
    unchecks_subcategory.click()
    time.sleep(1)

    #Unchecks the Remarks
    unchecks_remarks=context.browser.find_element(By.XPATH,xpaths.SKILLSET_UNCHECKS_REMARKS)
    unchecks_remarks.click()
    time.sleep(1)

    #Unchecks the Action
    unchecks_action=context.browser.find_element(By.XPATH,xpaths.SKILLSET_UNCHECKS_ACTION)
    unchecks_action.click()
    time.sleep(1)

    #Checks the No
    unchecks_no=context.browser.find_element(By.XPATH,xpaths.SKILLSET_UNCHECKS_NO)
    unchecks_no.click()
    time.sleep(1)

    #Checks the Name
    checks_name=context.browser.find_element(By.XPATH,xpaths.SKILLSET_UNCHECKS_NAME)
    checks_name.click()
    time.sleep(1)

    #Checks the Category
    checks_category=context.browser.find_element(By.XPATH,xpaths.SKILLSET_UNCHECKS_CATEGORY)
    checks_category.click()
    time.sleep(1)

    #Checks the SubCategory
    checks_subcategory=context.browser.find_element(By.XPATH,xpaths.SKILLSET_UNCHECKS_SUBCATEGORY)
    checks_subcategory.click()
    time.sleep(1)

    #Checks the Remarks
    checks_remarks=context.browser.find_element(By.XPATH,xpaths.SKILLSET_CHECKS_REMARKS)
    checks_remarks.click()
    time.sleep(1)
    
    #Checks the Action
    checks_action=context.browser.find_element(By.XPATH,xpaths.SKILLSET_CHECKS_ACTION)
    checks_action.click()
    time.sleep(1)

    #Click Total visibility column button to close
    visibility_column_button =context.browser.find_element(By.XPATH,xpaths.SKILLSET_VISIBILITY_COLUMN_BTN) 
    visibility_column_button.click()
    time.sleep(1)

@then('User should be able to see the results of total visibility column while checking/unchecking the skillset')
def step_impl(context):
    context.browser.implicitly_wait(1)
    header = context.browser.find_element(By.XPATH, xpaths.SKILLSET_RESULT)
    assert header.text == "Skill set"
    time.sleep(1)
    
#CREATE SKILLSET:

@when('User clicks on the add Skillset it takes to add Skillset page and enters the Skillset Name as "{Name}", Category as "{Category}", Sub category as "{Sub_Category}", Remarks as "{Remarks}"')
def enter_value(context,Name, Category, Sub_Category,Remarks):

    #Add skillset
    add_skillset_button =context.browser.find_element(By.XPATH, xpaths.SKILLSET_ADD_SKILLSET_BUTTON)
    add_skillset_button.click()
    time.sleep(1)
    
    #Enter skillset name
    skillset_name =context.browser.find_element(By.XPATH, xpaths.SKILLSET_NAME)
    skillset_name.send_keys(Name)
    time.sleep(1)
    
    #Enter skillset Category
    skillset_category =context.browser.find_element(By.XPATH, xpaths.SKILLSET_CATEGORY)
    skillset_category.send_keys(Category)
    time.sleep(1)
    
    #Enter skillset Subcategory
    skillset_subcategory =context.browser.find_element(By.XPATH, xpaths.SKILLSET_SUB_CATEGORY)
    skillset_subcategory.send_keys(Sub_Category)
    time.sleep(1)

    #Enter skillset Remarks
    skillset_remarks =context.browser.find_element(By.XPATH, xpaths.SKILLSET_REMARKS)
    skillset_remarks.send_keys(Remarks)
    time.sleep(1)

    #Save skillset
    skillset_save_button =context.browser.find_element(By.XPATH, xpaths.SKILLSET_SAVE)
    time.sleep(1)
    skillset_save_button.click()
    time.sleep(5)
    
@then('User should be able to create the Skillset and see the toast message as "Created Skillset Successfully"')
def step_impl(context):
    toast_message = context.browser.find_element(By.XPATH, xpaths.TOAST_ALERT)
    assert toast_message.text == "Success"
    time.sleep(1)

#CHECK SEARCH OPTION:
    
@when('User clicks on the searchfield and enters the created skillset Name as "{Name}"')  
def enter_value(context,Name):
    skillset_search =context.browser.find_element(By.XPATH, xpaths.SKILLSET_SEARCH)
    skillset_search.click()
    skillset_search.send_keys(Name)
    time.sleep(2)

@then('User should be able to see the results of Created Skillset')
def step_impl(context):
    context.browser.implicitly_wait(1)
    header = context.browser.find_element(By.XPATH, xpaths.SKILLSET_RESULT)
    assert header.text == "Skill set"
    time.sleep(1)

@when ('User clicks on the searchfield and enters the wrong skillset Name as "{Name}"')
def enter_value(context,Name):
    skillset_search =context.browser.find_element(By.XPATH, xpaths.SKILLSET_SEARCH)
    time.sleep(1)
    skillset_search .send_keys(Name)
    #time.sleep(2)

@then('User should be able to see the error message as "No skillsets found" in the skillset page')
def step_impl(context):
    error_message = context.browser.find_element(By.XPATH, xpaths.SKILLSET_SEARCH_ERROR)
    assert error_message.text == "Sorry"
    time.sleep(1)

#CREATE SKILLSET WITH SAME DETAILS:

@when('User clicks on add Skillset and enters the Skillset with same details the Name as "{Name}", Category as "{Category}", Sub category as "{Sub_Category}", Remarks as "{Remarks}"')
def enter_value(context,Name, Category, Sub_Category,Remarks):
    #context.browser.implicitly_wait(2)
    add_skillset_button =context.browser.find_element(By.XPATH, xpaths.SKILLSET_ADD_SKILLSET_BUTTON)
    add_skillset_button.click()
    time.sleep(1)
    
    skillset_name =context.browser.find_element(By.XPATH, xpaths.SKILLSET_NAME)
    skillset_name.send_keys(Name)
    #asset_typefield.keys(Keys.TAB)
    time.sleep(1)
    
    skillset_category =context.browser.find_element(By.XPATH, xpaths.SKILLSET_CATEGORY)
    skillset_category.send_keys(Category)
    #asset_namefield.keys(Keys.TAB)
    time.sleep(1)
    
    skillset_subcategory =context.browser.find_element(By.XPATH, xpaths.SKILLSET_SUB_CATEGORY)
    skillset_subcategory.send_keys(Sub_Category)
   # asset_capacityfield.keys(Keys.TAB)
    time.sleep(1)

    skillset_remarks =context.browser.find_element(By.XPATH, xpaths.SKILLSET_REMARKS)
    skillset_remarks.send_keys(Remarks)
   # asset_vehicleicon.keys(Keys.TAB)
    time.sleep(1)

    skillset_save_button =context.browser.find_element(By.XPATH, xpaths.SKILLSET_SAVE)
    time.sleep(1)
    skillset_save_button.click()
    time.sleep(5)

#CREATE SKILLSET WITH UNIQUE DETAILS:
@when('User enters the Skillset with unique details the Name as "{Name}", Category as "{Category}", Sub category as "{Sub_Category}", Remarks as "{Remarks}"')
def enter_value(context,Name, Category, Sub_Category,Remarks):
    
    skillset_name =context.browser.find_element(By.XPATH, xpaths.SKILLSET_NAME)
    skillset_name.send_keys(Keys.CONTROL + "a")
    skillset_name.send_keys(Keys.DELETE)
    skillset_name.send_keys(Name)
    time.sleep(1)
    
    skillset_category =context.browser.find_element(By.XPATH, xpaths.SKILLSET_CATEGORY)
    skillset_category.send_keys(Keys.CONTROL + "a")
    skillset_category.send_keys(Keys.DELETE)
    skillset_category.send_keys(Category)
    time.sleep(1)
    
    skillset_subcategory =context.browser.find_element(By.XPATH, xpaths.SKILLSET_SUB_CATEGORY)
    skillset_subcategory.send_keys(Keys.CONTROL + "a")
    skillset_subcategory.send_keys(Keys.DELETE)
    skillset_subcategory.send_keys(Sub_Category)
    time.sleep(1)

    skillset_remarks =context.browser.find_element(By.XPATH, xpaths.SKILLSET_REMARKS)
    skillset_remarks.send_keys(Keys.CONTROL + "a")
    skillset_remarks.send_keys(Keys.DELETE)
    skillset_remarks.send_keys(Remarks)
    time.sleep(1)

    skillset_save_button =context.browser.find_element(By.XPATH, xpaths.SKILLSET_SAVE)
    time.sleep(1)
    skillset_save_button.click()
    time.sleep(5)

@then('User should be able to see the error message as "skillset already exist in database"')
def step_impl(context):
    message = context.browser.find_element(By.XPATH, xpaths.TOAST_ALERT)
    assert message.text == "Skillset already exist in database"
    time.sleep(5)  
 
#CREATE SKILLSET WITH WITHOUT FILLING MANDATORY DETAILS:

@when('User clicks add Skillset and leave the Skillset fields empty the Name as " ", Category as " ", Sub category as " ", Remarks')
def enter_value(context):
    add_skillset_button =context.browser.find_element(By.XPATH, xpaths.SKILLSET_ADD_SKILLSET_BUTTON)
    add_skillset_button.click()
    time.sleep(1)
    
    skillset_name =context.browser.find_element(By.XPATH, xpaths.SKILLSET_NAME)
    skillset_name.send_keys()
    time.sleep(1)
    
    skillset_category =context.browser.find_element(By.XPATH, xpaths.SKILLSET_CATEGORY)
    skillset_category.send_keys()
    time.sleep(1)
    
    skillset_subcategory =context.browser.find_element(By.XPATH, xpaths.SKILLSET_SUB_CATEGORY)
    skillset_subcategory.send_keys()
    time.sleep(1)

    skillset_remarks =context.browser.find_element(By.XPATH, xpaths.SKILLSET_REMARKS)
    skillset_remarks.send_keys()
    time.sleep(1)

@then('User should be able to see the error message as "Required" in Add skillset page')
def step_impl(context):
    message = context.browser.find_element(By.XPATH, xpaths.SKILLSET_ERROR_MESSAGE)
    assert message.text == "Required"
    time.sleep(1)

#EDIT SKILLSET:

@when('User clicks on pencil icon it takes to edit Skillset page and enters the Skillset Name as "{Name}", Category as "{Category}", Sub category as "{Sub_Category}", Remarks as "{Remarks}"')
def enter_value(context,Name,Category, Sub_Category,Remarks):

    skillset_pencil_icon =context.browser.find_element(By.XPATH, xpaths.SKILLSET_PENCIL_ICON)
    skillset_pencil_icon.click()
    time.sleep(1)
    skillset_name =context.browser.find_element(By.XPATH, xpaths.SKILLSET_NAME)
    skillset_name.send_keys(Keys.CONTROL + "a")
    skillset_name.send_keys(Keys.DELETE)
    skillset_name.send_keys(Name)
    #asset_typefield.keys(Keys.TAB)
    time.sleep(1)
    
    skillset_category =context.browser.find_element(By.XPATH, xpaths.SKILLSET_CATEGORY)
    skillset_category.send_keys(Keys.CONTROL + "a")
    skillset_category.send_keys(Keys.DELETE)
    skillset_category.send_keys(Category)
    #asset_namefield.keys(Keys.TAB)
    time.sleep(1)
    
    skillset_subcategory =context.browser.find_element(By.XPATH, xpaths.SKILLSET_SUB_CATEGORY)
    skillset_subcategory.send_keys(Keys.CONTROL + "a")
    skillset_subcategory.send_keys(Keys.DELETE)
    skillset_subcategory.send_keys(Sub_Category)
   # asset_capacityfield.keys(Keys.TAB)
    time.sleep(1)

    skillset_remarks =context.browser.find_element(By.XPATH, xpaths.SKILLSET_REMARKS)
    skillset_remarks.send_keys(Keys.CONTROL + "a")
    skillset_remarks.send_keys(Keys.DELETE)
    skillset_remarks.send_keys(Remarks)
   # asset_vehicleicon.keys(Keys.TAB)
    time.sleep(1)

    skillset_save_button =context.browser.find_element(By.XPATH, xpaths.SKILLSET_SAVE)
    time.sleep(1)
    skillset_save_button.click()
    time.sleep(5)

@then('User should be able to edit all the changes in skillset and see the toast message as "Updated Skill Set Successfully"')
def step_impl(context):
    
    success_message = context.browser.find_element(By.XPATH, xpaths.TOAST_ALERT)
    assert success_message.text == "Success"
    time.sleep(1)


#DELETE SKILLSET:

@when('User clicks on the delete icon in skillset page')
def step_impl(context):
    delete_icon = context.browser.find_element(By.XPATH, xpaths.SKILLSET_DELETE_ICON_BUTTON)
    delete_icon.click()
    time.sleep(1)
    delete_popup_message = context.browser.find_element(By.XPATH, xpaths.SKILLSET_POPUP_MESSEGE)
    delete_popup_message.click()
    time.sleep(5)

@then('User should be able to delete the Skillset and see the toast message as "Deleted Skill Set Successfully"')  
def step_impl(context):
    delete_message = context.browser.find_element(By.XPATH, xpaths.TOAST_ALERT)
    assert delete_message.text == "Success"
    time.sleep(1)
