from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, xpaths

# given
# route to asset-type page 
@given('I am on the Field Personnel Page of a21-dev web application')
def step_impl(context):
    context.browser.get('https://a21-dev.integrum.global/pre-mission/field-personnel')
    time.sleep(1)

#Check Total Visibility Column:

@when('User clicks on the Total visibility column to unchecks/checks the visibility status of the Field Personnel')
def enter_value(context):

    #User click Total visibility column
    visibility_column_button =context.browser.find_element(By.XPATH,xpaths.FIELD_PERSONNEL_VISIBILITY_COLUMN_BTN)
    visibility_column_button.click()
    time.sleep(1)

    unchecks_no=context.browser.find_element(By.XPATH,xpaths.FIELD_PERSONNEL_UNCHECKS_NO) 
    unchecks_no.click()
    time.sleep(1)

    #Unchecks the Name
    unchecks_name=context.browser.find_element(By.XPATH,xpaths.FIELD_PERSONNEL_UNCHECKS_NAME) 
    unchecks_name.click()
    time.sleep(1)
   
    unchecks_contact_number=context.browser.find_element(By.XPATH,xpaths.FIELD_PERSONNEL_UNCHECKS_CONTACT_NUMBER) 
    unchecks_contact_number.click()
    time.sleep(1)

    unchecks_skillset=context.browser.find_element(By.XPATH,xpaths.FIELD_PERSONNEL_UNCHECKS_SKILLSET) 
    unchecks_skillset.click()
    time.sleep(1)
    
    unchecks_zone=context.browser.find_element(By.XPATH,xpaths.FIELD_PERSONNEL_UNCHECKS_ZONES) 
    unchecks_zone.click()
    time.sleep(1)

    unchecks_contract_date=context.browser.find_element(By.XPATH,xpaths.FIELD_PERSONNEL_UNCHECKS_CONTRACT_DATE) 
    unchecks_contract_date.click()
    time.sleep(1)

    unchecks_status=context.browser.find_element(By.XPATH,xpaths.FIELD_PERSONNEL_UNCHECKS_STATUS) 
    unchecks_status.click()
    time.sleep(1)

    unchecks_action=context.browser.find_element(By.XPATH,xpaths.FIELD_PERSONNEL_UNCHECKS_ACTION) 
    unchecks_action.click()
    time.sleep(1)

    checks_no=context.browser.find_element(By.XPATH,xpaths.FIELD_PERSONNEL_CHECKS_NO) 
    checks_no.click()
    time.sleep(1)

    #Unchecks the Name
    checks_name=context.browser.find_element(By.XPATH,xpaths.FIELD_PERSONNEL_CHECKS_NAME) 
    checks_name.click()
    time.sleep(1)
   
    checks_contact_number=context.browser.find_element(By.XPATH,xpaths.FIELD_PERSONNEL_CHECKS_CONTACT_NUMBER) 
    checks_contact_number.click()
    time.sleep(1)

    checks_skillset=context.browser.find_element(By.XPATH,xpaths.FIELD_PERSONNEL_CHECKS_SKILLSET) 
    checks_skillset.click()
    time.sleep(1)
    
    checks_zone=context.browser.find_element(By.XPATH,xpaths.FIELD_PERSONNEL_CHECKS_ZONES) 
    checks_zone.click()
    time.sleep(1)

    checks_contract_date=context.browser.find_element(By.XPATH,xpaths.FIELD_PERSONNEL_CHECKS_CONTRACT_DATE) 
    checks_contract_date.click()
    time.sleep(1)

    checks_status=context.browser.find_element(By.XPATH,xpaths.FIELD_PERSONNEL_CHECKS_STATUS) 
    checks_status.click()
    time.sleep(1)

    checks_action=context.browser.find_element(By.XPATH,xpaths.FIELD_PERSONNEL_CHECKS_ACTION) 
    checks_action.click()
    time.sleep(1)

    visibility_column_button =context.browser.find_element(By.XPATH,xpaths.FIELD_PERSONNEL_VISIBILITY_COLUMN_BTN)
    visibility_column_button.click()
    time.sleep(1)


@then('User should be able to see the results of total visibility column while checking/unchecking the Field Personnel')
def step_impl(context):
    context.browser.implicitly_wait(2)
    header = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_RESULT)
    assert header.text == "Field Personnel"
    time.sleep(1)

#CREATE FIELD PERSONNEL

@when('User clicks on the add Field Personnel it takes to add Field Personnel page and enters the Field Personnel Name as "{Name}", Contact Number as "{Contact_Number}", Email as "{Email}", Skillset, Zones, date filter by "filter_condition" and inputs "month_year" as MM-YYYY and "date" as DD and Status')
def step_impl(context, Name, Contact_Number,Email):
    for row in context.table:
        contract_start_date_month_year = row["contract_start_date_month_year"]
        contract_start_date_date = row["contract_start_date_date"]
        contract_end_date_month_year = row["contract_end_date_month_year"]
        contract_end_date_date = row["contract_end_date_date"]
     
    add_fieldpersonnel =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_ADD_BUTTON)
    add_fieldpersonnel.click()
    time.sleep(1)
    
    fieldpersonnel_name =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_NAME)
    fieldpersonnel_name.send_keys(Name)
    time.sleep(1)

    fieldpersonnel_contact =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CONTACT_NUMBER)
    fieldpersonnel_contact.send_keys(Contact_Number)
    time.sleep(1)
      
    fieldpersonnel_email =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_EMAIL)
    fieldpersonnel_email.send_keys(Email)
    time.sleep(1)

    fieldpersonnel_skillset =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SKILLSET_DROP_DOWN)
    fieldpersonnel_skillset.click()
    time.sleep(1)

    fieldpersonnel_skillset =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SKILLSET)
    fieldpersonnel_skillset.click()

    fieldpersonnel_zones =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_ZONES_DROP_DOWN)
    fieldpersonnel_zones.click()
    time.sleep(1)

    fieldpersonnel_zones =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_ZONE)
    fieldpersonnel_zones.click()

    # start date calendar
    input_field = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CONTRACT_START_DATE_OPTION)
    input_field.click()

    next_btn = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_NEXT_BTN)
  
    calendar_mm_yyyy = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_MM_YYYY)
    time.sleep(1)
    # select correct MM-YYYY
    while calendar_mm_yyyy.text != contract_start_date_month_year:
        next_btn.click()
        calendar_mm_yyyy = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_MM_YYYY)


    # select date
    date_element = context.browser.find_element(By.XPATH, f"//span[text()='{contract_start_date_date}']")
    date_element.click()
    time.sleep(1)

# end date calendar
    input_field = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CONTRACT_END_DATE_OPTION)
    input_field.click()

    next_btn = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_NEXT_BTN)
   
    calendar_mm_yyyy = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_END_MM_YYYY)
    time.sleep(1)

    # select correct MM-YYYY
    while calendar_mm_yyyy.text != contract_end_date_month_year:
        next_btn.click()
        calendar_mm_yyyy = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_END_MM_YYYY)


    # select date
    date_element = context.browser.find_element(By.XPATH, f"//span[text()='{contract_end_date_date}']")
    date_element.click()
    time.sleep(1)

    status_active =context.browser.find_element(By.XPATH,xpaths.FIELD_PERSONNEL_STATUS_ACTIVE)
    time.sleep(1)
    status_active.click()

    fieldpersonnel_save_button =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SAVE_BUTTON)
    time.sleep(1)
    fieldpersonnel_save_button.click()
    time.sleep(5)

@then('User should be able to create the Field Personnel and see the toast message as "Success"')
def step_impl(context):  
    success_message = context.browser.find_element(By.XPATH, xpaths.TOAST_ALERT)
    assert success_message.text == "Success"
    time.sleep(1)

#CHECK SEARCH OPTION 
    
@when ('User clicks on the searchfield and enters the created Field Personnel Name as "{Name}"')
def enter_value(context,Name):
    field_personnel_search =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SEARCH)
    field_personnel_search.click()
    time.sleep(1)
    field_personnel_search.send_keys(Name)
    time.sleep(3)
    
    
@then('User should be able to see the results of Created Field Personnel')
def step_impl(context):
    #context.browser.implicitly_wait(1)
    #verify the results of search option and the count relevant to the search option
    header = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_RESULT)
    assert header.text == "Field Personnel"
    time.sleep(1)
    

@when('User clicks on the searchfield and enters the wrong Field Personnel Name as "{Name}"')
def enter_value(context,Name):
    field_personnel_search_close =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SEARCH_CLOSE)
    field_personnel_search_close.click()
    time.sleep(2)

    field_personnel_search =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SEARCH)
    field_personnel_search.click()
    field_personnel_search.send_keys(Name)
    time.sleep(2)


@then('User should be able to see the error message as "No field personnels found" in the Field Personnel page')
def step_impl(context):
    error_message = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SEARCH_ERROR)
    assert error_message.text == "Sorry"
    

#SAME DETAILS
'''
@when('User clicks on the add Field Personnel and enters the Field Personnel with same details the Name as "{Name}", Contact Number as "{Contact_Number}", Email as "{Email}", Skillset, Zones, date filter by "filter_condition" and inputs "month_year" as MM-YYYY and "date" as DD, Shift and Status')
def step_impl(context, Name, Contact_Number,Email):
    for row in context.table:
        contract_start_date_month_year = row["contract_start_date_month_year"]
        contract_start_date_date = row["contract_start_date_date"]
        contract_end_date_month_year = row["contract_end_date_month_year"]
        contract_end_date_date = row["contract_end_date_date"]

    field_personnel_search_close =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SEARCH_CLOSE)
    field_personnel_search_close.click()
    time.sleep(2)
     #context.browser.implicitly_wait(2)
    add_fieldpersonnel =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_ADD_BUTTON)
    add_fieldpersonnel.click()
    time.sleep(1)
    
    fieldpersonnel_name =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_NAME)
    fieldpersonnel_name.send_keys(Name)
    time.sleep(1)

    fieldpersonnel_contact =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CONTACT_NUMBER)
    fieldpersonnel_contact.send_keys(Contact_Number)
    time.sleep(1)
      
    fieldpersonnel_email =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_EMAIL)
    fieldpersonnel_email.send_keys(Email)
    time.sleep(1)

    fieldpersonnel_skillset =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SKILLSET_DROP_DOWN)
    fieldpersonnel_skillset.click()
    time.sleep(1)

    fieldpersonnel_skillset =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SKILLSET)
    fieldpersonnel_skillset.click()

    fieldpersonnel_zones =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_ZONES_DROP_DOWN)
    fieldpersonnel_zones.click()
    time.sleep(1)

    fieldpersonnel_zones =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_ZONE)
    fieldpersonnel_zones.click()

        # start date calendar
    input_field = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CONTRACT_START_DATE_OPTION)
    input_field.click()

    prev_btn = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_PREV_BTN)
  
    calendar_mm_yyyy = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_MM_YYYY)
    time.sleep(1)
    # select correct MM-YYYY
    while calendar_mm_yyyy.text != contract_start_date_month_year:
        prev_btn.click()
        calendar_mm_yyyy = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_MM_YYYY)

    # select date
    date_element = context.browser.find_element(By.XPATH, f"//span[text()='{contract_start_date_date}']")
    date_element.click()
    time.sleep(1)

    # end date calendar
    input_field = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CONTRACT_END_DATE_OPTION)
    input_field.click()

    prev_btn = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_END_PREV_BTN)
   
    calendar_mm_yyyy = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_END_MM_YYYY)
    time.sleep(1)

    # select correct MM-YYYY
    while calendar_mm_yyyy.text != contract_end_date_month_year:
        prev_btn.click()
        calendar_mm_yyyy = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_END_MM_YYYY)


    # select date
    date_element = context.browser.find_element(By.XPATH, f"//span[text()='{contract_end_date_date}']")
    date_element.click()
    time.sleep(1)

    fieldpersonnel_shift =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SHIFT_DROP_DOWN)
    fieldpersonnel_shift.click()
    time.sleep(1)

    fieldpersonnel_shift =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SHIFT)
    fieldpersonnel_shift.click()

    status_active =context.browser.find_element(By.XPATH,xpaths.FIELD_PERSONNEL_STATUS_ACTIVE)
    time.sleep(1)
    status_active.click()

    fieldpersonnel_save_button =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SAVE_BUTTON)
    time.sleep(1)
    fieldpersonnel_save_button.click()
    time.sleep(3)

@when('User enters the Field Personnel with unique details the Name as "{Name}", Contact Number as "{Contact_Number}", Email as "{Email}", Skillset, Zones, date filter by "filter_condition" and inputs "month_year" as MM-YYYY and "date" as DD, Shift and Status')
def step_impl(context, Name, Contact_Number,Email):
    for row in context.table:
        contract_start_date_month_year = row["contract_start_date_month_year"]
        contract_start_date_date = row["contract_start_date_date"]
        contract_end_date_month_year = row["contract_end_date_month_year"]
        contract_end_date_date = row["contract_end_date_date"]

    fieldpersonnel_name =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_NAME)
    fieldpersonnel_name.send_keys(Keys.CONTROL + "a")
    fieldpersonnel_name.send_keys(Keys.DELETE)
    fieldpersonnel_name.send_keys(Name)
    time.sleep(1)

    fieldpersonnel_contact =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CONTACT_NUMBER)
    fieldpersonnel_contact.send_keys(Keys.CONTROL + "a")
    fieldpersonnel_contact.send_keys(Keys.DELETE)
    fieldpersonnel_contact.send_keys(Contact_Number)
    time.sleep(1)
      
    fieldpersonnel_email =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_EMAIL)
    fieldpersonnel_email.send_keys(Keys.CONTROL + "a")
    fieldpersonnel_email.send_keys(Keys.DELETE)
    fieldpersonnel_email.send_keys(Email)
    time.sleep(1)

    fieldpersonnel_skillset_clear =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SKILLSET_DROP_DOWN_CLEAR)
    fieldpersonnel_skillset_clear.click()
    time.sleep(1)

    fieldpersonnel_skillset =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SKILLSET_DROP_DOWN)
    fieldpersonnel_skillset.click()
    time.sleep(1)

    fieldpersonnel_skillset =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SKILLSET)
    fieldpersonnel_skillset.click()

    fieldpersonnel_zones_clear =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_ZONES_DROP_DOWN_CLEAR)
    fieldpersonnel_zones_clear.click()
    time.sleep(1)

    fieldpersonnel_zones =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_ZONES_DROP_DOWN)
    fieldpersonnel_zones.click()
    time.sleep(1)

    fieldpersonnel_zones =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_ZONE)
    fieldpersonnel_zones.click()

    # start date calendar
    input_field = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CONTRACT_START_DATE_OPTION)
    input_field.click()

    prev_btn = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_PREV_BTN)
  
    calendar_mm_yyyy = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_MM_YYYY)
    time.sleep(1)
    # select correct MM-YYYY
    while calendar_mm_yyyy.text != contract_start_date_month_year:
        prev_btn.click()
        calendar_mm_yyyy = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_MM_YYYY)

    # select date
    date_element = context.browser.find_element(By.XPATH, f"//span[text()='{contract_start_date_date}']")
    date_element.click()
    time.sleep(1)

    # end date calendar
    input_field = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CONTRACT_END_DATE_OPTION)
    input_field.click()

    prev_btn = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_END_PREV_BTN)
   
    calendar_mm_yyyy = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_END_MM_YYYY)
    time.sleep(1)

    # select correct MM-YYYY
    while calendar_mm_yyyy.text != contract_end_date_month_year:
        prev_btn.click()
        calendar_mm_yyyy = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_END_MM_YYYY)


    # select date
    date_element = context.browser.find_element(By.XPATH, f"//span[text()='{contract_end_date_date}']")
    date_element.click()
    time.sleep(1)

    fieldpersonnel_shift =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SHIFT_DROP_DOWN)
    fieldpersonnel_shift.click()
    time.sleep(1)

    fieldpersonnel_shift =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SHIFT)
    fieldpersonnel_shift.click()

    status_active =context.browser.find_element(By.XPATH,xpaths.FIELD_PERSONNEL_STATUS_ACTIVE)
    time.sleep(1)
    status_active.click()

    fieldpersonnel_save_button =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SAVE_BUTTON)
    time.sleep(1)
    fieldpersonnel_save_button.click()
    time.sleep(3)'''

@then('User should be able to see the error message as "User already exists"')
def step_impl(context):
    error_message = context.browser.find_element(By.XPATH, xpaths.TOAST_ALERT)
    assert error_message.text == "User already exists"
    time.sleep(1)
    close_toast_message = context.browser.find_element(By.XPATH, xpaths.TOAST_MESSAGE_CLOSE)
    close_toast_message.click()
    time.sleep(1)

@when('User clicks on the add Skillset and leave the Field Personnel fields empty the Name as "", Contact Number as "", Email as "", Skillset, Zones, Contract Start Date, Contract End Date, Shift and Status')
def step_impl(context):

    add_fieldpersonnel =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_ADD_BUTTON)
    add_fieldpersonnel.click()
    time.sleep(1)
    
    fieldpersonnel_name =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_NAME)
    fieldpersonnel_name.send_keys()
    time.sleep(1)

    fieldpersonnel_contact =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CONTACT_NUMBER)
    fieldpersonnel_contact.send_keys()
    time.sleep(1)
      
    fieldpersonnel_email =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_EMAIL)
    fieldpersonnel_email.send_keys()
    time.sleep(1)

    fieldpersonnel_skillset =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SKILLSET_DROP_DOWN)
    fieldpersonnel_skillset.click()
    time.sleep(1)

    fieldpersonnel_zones =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_ZONES_DROP_DOWN)
    fieldpersonnel_zones.click()
    time.sleep(1)

    fieldpersonnel_contract_start_date =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CONTRACT_START_DATE_OPTION)
    fieldpersonnel_contract_start_date.click()
    time.sleep(1)

    fieldpersonnel_contract_end_date =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CONTRACT_END_DATE_OPTION)
    fieldpersonnel_contract_end_date.click()
    time.sleep(1)

    # fieldpersonnel_shift =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SHIFT_DROP_DOWN)
    # fieldpersonnel_shift.click()
    # time.sleep(1)

    # fieldpersonnel_shift =context.browser.find_element(By.XPATH, ("//*[text()='Morning Shift']"))
    # fieldpersonnel_shift.click()

    status_active =context.browser.find_element(By.XPATH,xpaths.FIELD_PERSONNEL_STATUS_ACTIVE)
    time.sleep(1)
    status_active.click()

    fieldpersonnel_save_button =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SAVE_BUTTON)
    time.sleep(1)
    fieldpersonnel_save_button.click()
    time.sleep(5)

@then('User should be able to see the error message as "Required" in Add Field Personnel page') 
def step_impl(context):
 
    errormessage = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_ERROR_MESSAGE)
    assert errormessage.text == "Required"
    time.sleep(1)

#EDIT

@when('User clicks on the pencil icon it takes to edit Field Personnel page and enters the Field Personnel Name as "{Name}", Contact Number as "{Contact_Number}", Email as "{Email}", Skillset, Zones, date filter by "filter_condition" and inputs "month_year" as MM-YYYY and "date" as DD, Shift and Status')
def step_impl(context, Name, Contact_Number,Email):
    for row in context.table:
        contract_start_date_month_year = row["contract_start_date_month_year"]
        contract_start_date_date = row["contract_start_date_date"]
        contract_end_date_month_year = row["contract_end_date_month_year"]
        contract_end_date_date = row["contract_end_date_date"]

    #context.browser.implicitly_wait(2)
    fieldpersonnel_pencil_icon =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_PENCIL_ICON)
    fieldpersonnel_pencil_icon.click()
    time.sleep(1)
    
    fieldpersonnel_name =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_NAME)
    fieldpersonnel_name.send_keys(Keys.CONTROL + "a")
    fieldpersonnel_name.send_keys(Keys.DELETE)
    fieldpersonnel_name.send_keys(Name)
    time.sleep(1)

    fieldpersonnel_contact =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CONTACT_NUMBER)
    fieldpersonnel_contact.send_keys(Keys.CONTROL + "a")
    fieldpersonnel_contact.send_keys(Keys.DELETE)
    fieldpersonnel_contact.send_keys(Contact_Number)
    time.sleep(1)
      
    fieldpersonnel_email =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_EMAIL)
    fieldpersonnel_email.send_keys(Keys.CONTROL + "a")
    fieldpersonnel_email.send_keys(Keys.DELETE)
    fieldpersonnel_email.send_keys(Email)
    time.sleep(1)
    
    fieldpersonnel_skillset_clear =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SKILLSET_DROP_DOWN_CLEAR)
    fieldpersonnel_skillset_clear.click()
    time.sleep(1)

    fieldpersonnel_skillset_dropdown =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SKILLSET_DROP_DOWN)
    fieldpersonnel_skillset_dropdown.click()
    time.sleep(1)

    fieldpersonnel_skillset =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SKILLSET)
    fieldpersonnel_skillset.click()
    
    # fieldpersonnel_zones_clear =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_ZONES_DROP_DOWN_CLEAR)
    # fieldpersonnel_zones_clear.click()
    # time.sleep(1)

    fieldpersonnel_zones_dropdown =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_ZONES_DROP_DOWN)
    fieldpersonnel_zones_dropdown.click()
    time.sleep(1)

    fieldpersonnel_zones =context.browser.find_element (By.XPATH, xpaths.FIELD_PERSONNEL_ZONE)
    fieldpersonnel_zones.click()

    # start date calendar
    input_field = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CONTRACT_START_DATE_OPTION)
    input_field.click()

    prev_btn = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_PREV_BTN)
  
    calendar_mm_yyyy = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_MM_YYYY)
    time.sleep(1)
    # select correct MM-YYYY
    while calendar_mm_yyyy.text != contract_start_date_month_year:
        prev_btn.click()
        calendar_mm_yyyy = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_MM_YYYY)

    # select date
    date_element = context.browser.find_element(By.XPATH, f"//span[text()='{contract_start_date_date}']")
    date_element.click()
    time.sleep(1)

# end date calendar
    input_field = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CONTRACT_END_DATE_OPTION)
    input_field.click()

    prev_btn = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_END_PREV_BTN)
   
    calendar_mm_yyyy = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_END_MM_YYYY)
    time.sleep(1)

    # select correct MM-YYYY
    while calendar_mm_yyyy.text != contract_end_date_month_year:
        prev_btn.click()
        calendar_mm_yyyy = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_END_MM_YYYY)


    # select date
    date_element = context.browser.find_element(By.XPATH, f"//span[text()='{contract_end_date_date}']")
    date_element.click()
    time.sleep(1)

    fieldpersonnel_shift =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SHIFT_DROP_DOWN)
    fieldpersonnel_shift.click()
    time.sleep(1)

    fieldpersonnel_shift =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SHIFT)
    fieldpersonnel_shift.click()

    status_active =context.browser.find_element(By.XPATH,xpaths.FIELD_PERSONNEL_STATUS_ACTIVE)
    time.sleep(1)
    status_active.click()

    fieldpersonnel_save_button =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SAVE_BUTTON)
    time.sleep(1)
    fieldpersonnel_save_button.click()
    time.sleep(5)

@then('User should be able to edit all the changes in Field Personnel and see the toast message as "Success"')
def step_impl(context):
    success_message = context.browser.find_element(By.XPATH, xpaths.TOAST_ALERT)
    assert success_message.text == "Success"
    time.sleep(1)

#phone number and status:

@when('User clicks on the pencil icon it takes to edit Field Personnel page and enters the Field Personnel Name as "{Name}", Thailand Contact Number as "{Contact_Number}", Email as "{Email}", Skillset, Zones, date filter by "filter_condition" and inputs "month_year" as MM-YYYY and "date" as DD, Shift and Status')
def step_impl(context, Name, Contact_Number,Email):
    for row in context.table:
        contract_start_date_month_year = row["contract_start_date_month_year"]
        contract_start_date_date = row["contract_start_date_date"]
        contract_end_date_month_year = row["contract_end_date_month_year"]
        contract_end_date_date = row["contract_end_date_date"]

    #context.browser.implicitly_wait(2)
    fieldpersonnel_pencil_icon =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_PENCIL_ICON)
    fieldpersonnel_pencil_icon.click()
    time.sleep(1)
    
    fieldpersonnel_name =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_NAME)
    fieldpersonnel_name.send_keys(Keys.CONTROL + "a")
    fieldpersonnel_name.send_keys(Keys.DELETE)
    fieldpersonnel_name.send_keys(Name)
    time.sleep(1)

    fieldpersonnel_contact =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CONTACT_NUMBER)
    fieldpersonnel_contact.send_keys(Keys.CONTROL + "a")
    fieldpersonnel_contact.send_keys(Keys.DELETE)
    fieldpersonnel_contact.send_keys(Contact_Number)
    time.sleep(1)
      
    fieldpersonnel_email =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_EMAIL)
    fieldpersonnel_email.send_keys(Keys.CONTROL + "a")
    fieldpersonnel_email.send_keys(Keys.DELETE)
    fieldpersonnel_email.send_keys(Email)
    time.sleep(1)

    fieldpersonnel_skillset_clear =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SKILLSET_DROP_DOWN_CLEAR)
    fieldpersonnel_skillset_clear.click()
    time.sleep(1)

    fieldpersonnel_skillset_dropdown =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SKILLSET_DROP_DOWN)
    fieldpersonnel_skillset_dropdown.click()
    time.sleep(1)

    fieldpersonnel_skillset =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SKILLSET)
    fieldpersonnel_skillset.click()
    
    # fieldpersonnel_zones_clear =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_ZONES_DROP_DOWN_CLEAR)
    # fieldpersonnel_zones_clear.click()
    # time.sleep(1)

    fieldpersonnel_zones_dropdown =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_ZONES_DROP_DOWN)
    fieldpersonnel_zones_dropdown.click()
    time.sleep(2)

    fieldpersonnel_zones =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_ZONE)
    fieldpersonnel_zones.click()
    
    # start date calendar
    input_field = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CONTRACT_START_DATE_OPTION)
    input_field.click()

    prev_btn = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_PREV_BTN)
  
    calendar_mm_yyyy = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_MM_YYYY)
    time.sleep(1)
    # select correct MM-YYYY
    while calendar_mm_yyyy.text != contract_start_date_month_year:
        prev_btn.click()
        calendar_mm_yyyy = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_MM_YYYY)


    # select date
    date_element = context.browser.find_element(By.XPATH, f"//span[text()='{contract_start_date_date}']")
    date_element.click()
    time.sleep(1)

# end date calendar
    input_field = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CONTRACT_END_DATE_OPTION)
    input_field.click()

    prev_btn = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_END_PREV_BTN)
   
    calendar_mm_yyyy = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_END_MM_YYYY)
    time.sleep(1)

    # select correct MM-YYYY
    while calendar_mm_yyyy.text != contract_end_date_month_year:
        prev_btn.click()
        calendar_mm_yyyy = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CALENDAR_END_MM_YYYY)


    # select date
    date_element = context.browser.find_element(By.XPATH, f"//span[text()='{contract_end_date_date}']")
    date_element.click()
    time.sleep(1)

    fieldpersonnel_shift =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SHIFT_DROP_DOWN)
    fieldpersonnel_shift.click()
    time.sleep(1)

    fieldpersonnel_shift =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SHIFT)
    fieldpersonnel_shift.click()

    fieldpersonnel_status_active =context.browser.find_element(By.XPATH,xpaths.FIELD_PERSONNEL_STATUS_ACTIVE)
    time.sleep(1)
    fieldpersonnel_status_active.click()

    fieldpersonnel_status_inactive =context.browser.find_element(By.XPATH,xpaths.FIELD_PERSONNEL_STATUS_INACTIVE)
    time.sleep(1)
    fieldpersonnel_status_inactive.click()

    fieldpersonnel_save_button =context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_SAVE_BUTTON)
    time.sleep(1)
    fieldpersonnel_save_button.click()
    time.sleep(5)

@then('User should be able to edit the phone Number and status in the Field Personnel and see the toast message as "Success"')
def step_impl(context):
    updatemessage = context.browser.find_element(By.XPATH, xpaths.TOAST_ALERT)
    assert updatemessage.text == "Success"
    time.sleep(1)

#BLOCK THE FIELD PERSONNEL:

@when('User clicks on the block/unblock icon in Field Personnel page')
def step_impl(context):
    block_icon = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_BLOCK_ICON_BUTTON)
    block_icon.click()
    time.sleep(1)

    block_popup_message = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_POPUP_MESSEGE)
    block_popup_message.click()
    time.sleep(2)

    fieldpersonnel_cancel_button = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_CANCEL_BUTTON)
    fieldpersonnel_cancel_button.click()
    time.sleep(3)

@then('User able to activate/deactivate the Field Personnel')  
def step_impl(context):
    error_message = context.browser.find_element(By.XPATH, xpaths.FIELD_PERSONNEL_UPDATED_MESSAGE)
    assert error_message.text == "Sorry"
    time.sleep(1)
 

