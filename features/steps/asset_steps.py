from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, xpaths


@given('I am on the asset page of integrum mobility web application')
def step_impl(context):
    context.browser.get('https://boonrawd-dev.integrum.global/pre-mission/asset')
    time.sleep(2)
    #context.maximize_window()
    context.browser.implicitly_wait(2)

#SEARCH OPTION AND VISIBILITY COLUMN CHECK

@when('User clicks on the Total visibility column to unchecks/checks the visibility status of the asset')
def enter_value(context):
    # Total visibility column
    visibility_column_btn =context.browser.find_element(By.XPATH,xpaths.ASSET_VISIBILITY_COLUMN_BTN)
    visibility_column_btn.click()
    time.sleep(1)

   #  #Unchecks the visibility column
   #  unchecks_vehicle_manufacturer=context.browser.find_element(By.XPATH,xpaths.ASSET_VEHICLE_MANUFACTURER_CHECKBOX)
   #  unchecks_vehicle_manufacturer.click()
   #  time.sleep(1)

   #  unchecks_vehicle_model=context.browser.find_element(By.XPATH,xpaths.ASSET_VEHICLE_MODEL_CHECKBOX)
   #  unchecks_vehicle_model.click()
   #  time.sleep(1)

   #  unchecks_vehicle_name=context.browser.find_element(By.XPATH,xpaths.ASSET_VEHICLE_NAME_CHECKBOX)
   #  unchecks_vehicle_name.click()
   #  time.sleep(1)

    unchecks_licenseplate=context.browser.find_element(By.XPATH,xpaths.ASSET_LICENSE_PLATE_CHECKBOX)
    unchecks_licenseplate.click()
    time.sleep(1)

    unchecks_vehicle_type=context.browser.find_element(By.XPATH,xpaths.ASSET_VEHICLE_TYPE_CHECKBOX)
    unchecks_vehicle_type.click()
    time.sleep(1)

    unchecks_start_location=context.browser.find_element(By.XPATH,xpaths.ASSET_START_LOCATION_CHECKBOX)
    unchecks_start_location.click()
    time.sleep(1)

    unchecks_end_location=context.browser.find_element(By.XPATH,xpaths.ASSET_END_LOCATION_CHECKBOX)
    unchecks_end_location.click()
    time.sleep(1)

    unchecks_field_personnel=context.browser.find_element(By.XPATH,xpaths.ASSET_FIELD_PERSONNEL_CHECKBOX)
    unchecks_field_personnel.click()
    time.sleep(1)

    unchecks_status=context.browser.find_element(By.XPATH,xpaths.ASSET_STATUS_CHECKBOX)
    unchecks_status.click()
    time.sleep(1)

    unchecks_action=context.browser.find_element(By.XPATH,xpaths.ASSET_ACTION_CHECKBOX)
    unchecks_action.click()
    time.sleep(1)

    #Checks the visibility column
    checks_vehicle_manufacturer=context.browser.find_element(By.XPATH,xpaths.ASSET_VEHICLE_MANUFACTURER_CHECKBOX)
    checks_vehicle_manufacturer.click()
    time.sleep(1)

    checks_vehicle_model=context.browser.find_element(By.XPATH,xpaths.ASSET_VEHICLE_MODEL_CHECKBOX)
    checks_vehicle_model.click()
    time.sleep(1)

    checks_vehicle_name=context.browser.find_element(By.XPATH,xpaths.ASSET_VEHICLE_NAME_CHECKBOX)
    checks_vehicle_name.click()
    time.sleep(1)

    checks_licenseplate=context.browser.find_element(By.XPATH,xpaths.ASSET_LICENSE_PLATE_CHECKBOX)
    checks_licenseplate.click()
    time.sleep(1)

    checks_vehicle_type=context.browser.find_element(By.XPATH,xpaths.ASSET_VEHICLE_TYPE_CHECKBOX)
    checks_vehicle_type.click()
    time.sleep(1)

    checks_start_location=context.browser.find_element(By.XPATH,xpaths.ASSET_START_LOCATION_CHECKBOX)
    checks_start_location.click()
    time.sleep(1)

    checks_end_location=context.browser.find_element(By.XPATH,xpaths.ASSET_END_LOCATION_CHECKBOX)
    checks_end_location.click()
    time.sleep(1)

    checks_field_personnel=context.browser.find_element(By.XPATH,xpaths.ASSET_FIELD_PERSONNEL_CHECKBOX)
    checks_field_personnel.click()
    time.sleep(1)

    checks_status=context.browser.find_element(By.XPATH,xpaths.ASSET_STATUS_CHECKBOX)
    checks_status.click()
    time.sleep(1)

    checks_action=context.browser.find_element(By.XPATH,xpaths.ASSET_ACTION_CHECKBOX)
    checks_action.click()
    time.sleep(1)

    visibility_column_btn =context.browser.find_element(By.XPATH,xpaths.ASSET_VISIBILITY_COLUMN_BTN)
    visibility_column_btn.click()
    time.sleep(1)

   
@then('User should be able to see the results of total visibility column while checking/unchecking the asset')
def step_impl(context):
    context.browser.implicitly_wait(2)
    header = context.browser.find_element(By.XPATH, xpaths.ASSET_RESULT)
    assert header.text == "Asset"
    time.sleep(1)


#CREATE ASSET 

@when('User clicks on the add asset it takes to add asset page and enters the asset Vehicle Manufacturer as "{Vehicle_Manufacturer}", Vehicle Model as "{Vehicle_Model}", Vehicle Type as " ", Vehicle Company as "{Vehicle_Company}", Register Number as"{Register_Number}", Depot Start, Depot End, License Plate as "{License_Plate}" and Status')
def step_impl(context, Vehicle_Manufacturer,Vehicle_Model,Vehicle_Company,Register_Number,License_Plate):
     #context.browser.implicitly_wait(2)
    add_asset_button =context.browser.find_element(By.XPATH, xpaths.ASSET_ADD_ASSET_BUTTON)
    add_asset_button.click()
    time.sleep(1)
    
    asset_vehicle_manufacturer =context.browser.find_element(By.XPATH, xpaths.ASSET_VEHICLE_MANUFACTURER)
    asset_vehicle_manufacturer.send_keys(Vehicle_Manufacturer)
 #  asset_vehicle_manufacturer.keys(Keys.TAB)
    time.sleep(1)

    asset_vehicle_model =context.browser.find_element(By.XPATH, xpaths.ASSET_VEHICLE_MODEL)
    asset_vehicle_model.send_keys(Vehicle_Model)
 #  asset_vehicle_manufacturer.keys(Keys.TAB)
    time.sleep(1)
    
    asset_vehicle_type =context.browser.find_element(By.XPATH, xpaths.ASSET_VEHICLE_TYPE_DROP_DOWN)
    asset_vehicle_type.click()
    time.sleep(1)

    asset_vehicle_type_option =context.browser.find_element(By.XPATH, xpaths.ASSET_VEHICLE_TYPE_OPTION)
    asset_vehicle_type_option.click()


    asset_vehicle_company =context.browser.find_element(By.XPATH, xpaths.ASSET_VEHICLE_COMPANY)
    asset_vehicle_company.send_keys(Vehicle_Company)
    time.sleep(1)

    asset_register_number =context.browser.find_element(By.XPATH, xpaths.ASSET_REGISTER_NUMBER)
    asset_register_number.send_keys(Register_Number)
    time.sleep(1)

    Depot_start =context.browser.find_element(By.XPATH,xpaths.ASSET_DEPOT_START)
    Depot_start.click()
        
    Depot_start_option =context.browser.find_element(By.XPATH, xpaths.ASSET_DEPOT_START_OPTIONS)
    Depot_start_option.click() 

    Depot_end =context.browser.find_element(By.XPATH,xpaths.ASSET_DEPOT_END)
    time.sleep(1)
    Depot_end.click()
    
    Depot_End =context.browser.find_element(By.ID, "react-select-4-listbox")
    time.sleep(1)
    Depot_End.click()

    asset_license_plate =context.browser.find_element(By.XPATH, xpaths.ASSET_LICENSE_PLATE)
    asset_license_plate.send_keys(License_Plate)
 #  asset_vehicle_manufacturer.keys(Keys.TAB)
    time.sleep(1)

    status_active =context.browser.find_element(By.XPATH,xpaths.ASSET_STATUS_ACTIVE)
    time.sleep(1)
    status_active.click()

    asset_save_button =context.browser.find_element(By.XPATH, xpaths.ASSET_SAVE_BUTTON)
    time.sleep(1)
    asset_save_button.click()
    time.sleep(5)

    
@then('User should be able to create the asset and see the toast message as "Created asset Successfully"')
def step_impl(context):
   success_message = context.browser.find_element(By.XPATH, xpaths.TOAST_ALERT)
   assert success_message.text == "Success"
   time.sleep(1)

  
@when('User clicks on the searchfield and enters the created asset License Plate as "{License_Plate}"')
def step_impl(context, License_Plate):
    asset_search =context.browser.find_element(By.XPATH, xpaths.ASSET_SEARCH)
   #searchfield.click()
    asset_search.send_keys(License_Plate)
    time.sleep(3)

@then('User should be able to see the results of Created asset')
def step_impl(context):
    context.browser.implicitly_wait(2)
    #verify the results of search option and the count relevant to the search option
    header = context.browser.find_element(By.XPATH, xpaths.ASSET_RESULT)
    assert header.text == "Asset"
    time.sleep(1)
    
#SEARCH OPTION CHECK

@when ('User clicks on the searchfield and enters the wrong asset License Plate as "{License_Plate}"')
def enter_value(context, License_Plate):
    asset_search =context.browser.find_element(By.XPATH, xpaths.ASSET_SEARCH)
   # time.sleep(2)
    asset_search.send_keys(License_Plate)
    time.sleep(2)

@then('User should be able to see the error message as "No assets found" in the asset page')
def step_impl(context):
    error_message = context.browser.find_element(By.XPATH, xpaths.ASSET_SEARCH_ERROR)
    assert error_message.text == "Sorry"
    #time.Sleep(2)
    
#CREATE ASSET WITH SAME DETAILS

@when('User clicks on the add asset and enters the asset with same details the Vehicle Manufacturer as "{Vehicle_Manufacturer}", Vehicle Model as "{Vehicle_Model}", Vehicle Type as " ", Vehicle Company as "{Vehicle_Company}", Register Number as"{Register_Number}", Depot Start, Depot End, License Plate as "{License_Plate}" and Status')
def step_impl(context, Vehicle_Manufacturer,Vehicle_Model,Vehicle_Company,Register_Number,License_Plate):
     #context.browser.implicitly_wait(2)
    add_asset_button =context.browser.find_element(By.XPATH, xpaths.ASSET_ADD_ASSET_BUTTON)
    add_asset_button.click()
    time.sleep(1)
    
    asset_vehicle_manufacturer =context.browser.find_element(By.XPATH, xpaths.ASSET_VEHICLE_MANUFACTURER)
    asset_vehicle_manufacturer.send_keys(Vehicle_Manufacturer)
 #  asset_vehicle_manufacturer.keys(Keys.TAB)
    time.sleep(1)

    asset_vehicle_model =context.browser.find_element(By.XPATH, xpaths.ASSET_VEHICLE_MODEL)
    asset_vehicle_model.send_keys(Vehicle_Model)
 #  asset_vehicle_manufacturer.keys(Keys.TAB)
    time.sleep(1)
    
    asset_vehicle_type =context.browser.find_element(By.XPATH, xpaths.ASSET_VEHICLE_TYPE_DROP_DOWN)
    asset_vehicle_type.click()
    time.sleep(1)
    
    asset_vehicle_type_option =context.browser.find_element(By.XPATH, xpaths.ASSET_VEHICLE_TYPE_OPTION)
    asset_vehicle_type_option.click()

    asset_vehicle_company =context.browser.find_element(By.XPATH, xpaths.ASSET_VEHICLE_COMPANY)
    asset_vehicle_company.send_keys(Vehicle_Company)
 #  asset_vehicle_manufacturer.keys(Keys.TAB)
    time.sleep(1)

    asset_register_number =context.browser.find_element(By.XPATH, xpaths.ASSET_REGISTER_NUMBER)
    asset_register_number.send_keys(Register_Number)
 #  asset_vehicle_manufacturer.keys(Keys.TAB)
    time.sleep(1)


    Depot_start =context.browser.find_element(By.XPATH,xpaths.ASSET_DEPOT_START)
    Depot_start.click()
    
    Depot_start_option =context.browser.find_element(By.XPATH, xpaths.ASSET_DEPOT_START_OPTIONS)
    Depot_start_option.click() 


    Depot_end =context.browser.find_element(By.XPATH,xpaths.ASSET_DEPOT_END)
    time.sleep(1)
    Depot_end.click()
    
    Depot_End =context.browser.find_element(By.ID, "react-select-4-listbox")
    time.sleep(1)
    Depot_End.click()

    asset_license_plate =context.browser.find_element(By.XPATH, xpaths.ASSET_LICENSE_PLATE)
    asset_license_plate.send_keys(License_Plate)
 #  asset_vehicle_manufacturer.keys(Keys.TAB)
    time.sleep(1)

    status_active =context.browser.find_element(By.XPATH,xpaths.ASSET_STATUS_ACTIVE)
    time.sleep(1)
    status_active.click()

    asset_save_button =context.browser.find_element(By.XPATH, xpaths.ASSET_SAVE_BUTTON)
    time.sleep(1)
    asset_save_button.click()
    time.sleep(5)

@when('User enters the asset with unique details the Vehicle Manufacturer as "{Vehicle_Manufacturer}", Vehicle Model as "{Vehicle_Model}", Vehicle Type as " ", Vehicle Company as "{Vehicle_Company}", Register Number as"{Register_Number}", Depot Start, Depot End, License Plate as "{License_Plate}" and Status')
def step_impl(context, Vehicle_Manufacturer,Vehicle_Model,Vehicle_Company,Register_Number,License_Plate):
 
    asset_vehicle_manufacturer =context.browser.find_element(By.XPATH, xpaths.ASSET_VEHICLE_MANUFACTURER)
    asset_vehicle_manufacturer.send_keys(Keys.CONTROL + "a")
    asset_vehicle_manufacturer.send_keys(Keys.DELETE)
    asset_vehicle_manufacturer.send_keys(Vehicle_Manufacturer)
 #  asset_vehicle_manufacturer.keys(Keys.TAB)
    time.sleep(1)

    asset_vehicle_model =context.browser.find_element(By.XPATH, xpaths.ASSET_VEHICLE_MODEL)
    asset_vehicle_model.send_keys(Keys.CONTROL + "a")
    asset_vehicle_model.send_keys(Keys.DELETE)
    asset_vehicle_model.send_keys(Vehicle_Model)
 #  asset_vehicle_manufacturer.keys(Keys.TAB)
    time.sleep(1)
    
   #  asset_vehicle_type =context.browser.find_element(By.XPATH, xpaths.ASSET_VEHICLE_TYPE_DROP_DOWN)
   #  asset_vehicle_type.click()
   #  time.sleep(1)
    
   #  asset_vehicle_type_option =context.browser.find_element(By.XPATH, ("//*[text()='Bike']"))
   #  asset_vehicle_type_option.click()

    asset_vehicle_company =context.browser.find_element(By.XPATH, xpaths.ASSET_VEHICLE_COMPANY)
    asset_vehicle_company.send_keys(Keys.CONTROL + "a")
    asset_vehicle_company.send_keys(Keys.DELETE)
    asset_vehicle_company.send_keys(Vehicle_Company)
 #  asset_vehicle_manufacturer.keys(Keys.TAB)
    time.sleep(1)

    asset_register_number =context.browser.find_element(By.XPATH, xpaths.ASSET_REGISTER_NUMBER)
    asset_register_number.send_keys(Keys.CONTROL + "a")
    asset_register_number.send_keys(Keys.DELETE)
    asset_register_number.send_keys(Register_Number)
 #  asset_vehicle_manufacturer.keys(Keys.TAB)
    time.sleep(1)


    asset_license_plate =context.browser.find_element(By.XPATH, xpaths.ASSET_LICENSE_PLATE)
    asset_license_plate.send_keys(Keys.CONTROL + "a")
    asset_license_plate.send_keys(Keys.DELETE)
    asset_license_plate.send_keys(License_Plate)
 #  asset_vehicle_manufacturer.keys(Keys.TAB)
    time.sleep(1)

    status_active =context.browser.find_element(By.XPATH,xpaths.ASSET_STATUS_ACTIVE)
    time.sleep(1)
    status_active.click()

    asset_save_button =context.browser.find_element(By.XPATH, xpaths.ASSET_SAVE_BUTTON)
    time.sleep(1)
    asset_save_button.click()
    time.sleep(5)

@then('User should be able to see the error message as "Vehicle type Name already exists"')
def step_impl(context):
    
    error_message = context.browser.find_element(By.XPATH, xpaths.TOAST_ALERT)
    assert error_message.text == "Vehicle is already exists with same License plate"
    time.sleep(1)

#WITHOUT FILLING MANDATORY DETAILS:

@when('User clicks add asset and leave the asset fields empty the Vehicle Manufacturer as "", Vehicle Model as "", Vehicle Type as "", Vehicle Company as "", Register Number "", Deport Start, Depot End, License Plate "" and Status')
def step_impl(context):
     #context.browser.implicitly_wait(2)
    add_asset_button =context.browser.find_element(By.XPATH, xpaths.ASSET_ADD_ASSET_BUTTON)
    add_asset_button.click()
    time.sleep(1)
    
    asset_vehicle_manufacturer =context.browser.find_element(By.XPATH, xpaths.ASSET_VEHICLE_MANUFACTURER)
    asset_vehicle_manufacturer.send_keys()
 #  asset_vehicle_manufacturer.keys(Keys.TAB)
    time.sleep(1)

    asset_vehicle_model =context.browser.find_element(By.XPATH, xpaths.ASSET_VEHICLE_MODEL)
    asset_vehicle_model.send_keys()
 #  asset_vehicle_manufacturer.keys(Keys.TAB)
    time.sleep(1)
     
    asset_vehicle_type =context.browser.find_element(By.XPATH, xpaths.ASSET_VEHICLE_TYPE_DROP_DOWN)
    asset_vehicle_type.click()
    time.sleep(1)

    asset_vehicle_type_option =context.browser.find_element(By.XPATH, xpaths.ASSET_VEHICLE_TYPE_OPTION)
    asset_vehicle_type_option.click()

    asset_vehicle_company =context.browser.find_element(By.XPATH, xpaths.ASSET_VEHICLE_COMPANY)
    asset_vehicle_company.send_keys()
 #  asset_vehicle_manufacturer.keys(Keys.TAB)
    time.sleep(1)

    asset_register_number =context.browser.find_element(By.XPATH, xpaths.ASSET_REGISTER_NUMBER)
    asset_register_number.send_keys()
 #  asset_vehicle_manufacturer.keys(Keys.TAB)
    time.sleep(1)


    Depot_start =context.browser.find_element(By.XPATH,xpaths.ASSET_DEPOT_START)
    Depot_start.click()
     
    Depot_start_option =context.browser.find_element(By.XPATH, xpaths.ASSET_DEPOT_START_OPTIONS)
    Depot_start_option.click() 

    Depot_end =context.browser.find_element(By.XPATH,xpaths.ASSET_DEPOT_END)
    time.sleep(2)
    Depot_end.click()
    
    Depot_End =context.browser.find_element(By.ID, "react-select-4-listbox")
    time.sleep(1)
    Depot_End.click()

    asset_license_plate =context.browser.find_element(By.XPATH, xpaths.ASSET_LICENSE_PLATE)
    asset_license_plate.send_keys()
 #  asset_vehicle_manufacturer.keys(Keys.TAB)
    time.sleep(1)

    status_active =context.browser.find_element(By.XPATH,xpaths.ASSET_STATUS_ACTIVE)
    time.sleep(1)
    status_active.click()

    asset_save_button =context.browser.find_element(By.XPATH, xpaths.ASSET_SAVE_BUTTON)
    time.sleep(1)
    asset_save_button.click()
    time.sleep(1)

@then('User see the error message like "Required" in asset')
def step_impl(context):
    
    error_message = context.browser.find_element(By.XPATH, xpaths.ASSET_ERROR_MESSAGE)
    assert error_message.text == "Required"
    time.sleep(1)



#EDIT THE CHANGES:

@when('User clicks pencil icon it takes to edit asset page and enters the asset Vehicle Manufacturer as "{Vehicle_Manufacturer}", Vehicle Model as "{Vehicle_Model}", Vehicle Type as " ", Vehicle Company as "{Vehicle_Company}", Register Number as"{Register_Number}", Depot Start, Depot End, License Plate as "{License_Plate}" and Status')
def step_impl(context, Vehicle_Manufacturer,Vehicle_Model,Vehicle_Company,Register_Number,License_Plate):
     #context.browser.implicitly_wait(2)
    asset_pencil_icon =context.browser.find_element(By.XPATH, xpaths.ASSET_PENCIL_ICON)
    asset_pencil_icon.click()
    time.sleep(1)
    
    asset_vehicle_manufacturer =context.browser.find_element(By.XPATH, xpaths.ASSET_VEHICLE_MANUFACTURER)
    asset_vehicle_manufacturer.send_keys(Keys.CONTROL + "a")
    asset_vehicle_manufacturer.send_keys(Keys.DELETE)
    asset_vehicle_manufacturer.send_keys(Vehicle_Manufacturer)
    time.sleep(1)
 #  asset_vehicle_manufacturer.keys(Keys.TAB)
    time.sleep(1)

    asset_vehicle_model =context.browser.find_element(By.XPATH, xpaths.ASSET_VEHICLE_MODEL)
    asset_vehicle_model.send_keys(Keys.CONTROL + "a")
    asset_vehicle_model.send_keys(Keys.DELETE)
    asset_vehicle_model.send_keys(Vehicle_Model)
 #  asset_vehicle_manufacturer.keys(Keys.TAB)
    time.sleep(1)
        
    asset_vehicle_type =context.browser.find_element(By.XPATH, xpaths.ASSET_VEHICLE_TYPE_DROP_DOWN)
    asset_vehicle_type.click()
    time.sleep(1)

    asset_vehicle_company =context.browser.find_element(By.XPATH, xpaths.ASSET_VEHICLE_COMPANY)
    asset_vehicle_company.send_keys(Keys.CONTROL + "a")
    asset_vehicle_company.send_keys(Keys.DELETE)
    asset_vehicle_company.send_keys(Vehicle_Company)
 #  asset_vehicle_manufacturer.keys(Keys.TAB)
    time.sleep(1)

    asset_register_number =context.browser.find_element(By.XPATH, xpaths.ASSET_REGISTER_NUMBER)
    asset_register_number.send_keys(Keys.CONTROL + "a")
    asset_register_number.send_keys(Keys.DELETE)
    asset_register_number.send_keys(Register_Number)
 #  asset_vehicle_manufacturer.keys(Keys.TAB)
    time.sleep(1)


    Depot_start =context.browser.find_element(By.XPATH,xpaths.ASSET_DEPOT_START)
    Depot_start.click()


    Depot_end =context.browser.find_element(By.XPATH,xpaths.ASSET_DEPOT_END)
    time.sleep(1)
    Depot_end.click()
    
    #Depot_End =context.browser.find_element(By.ID, "react-select-4-listbox")
    #time.sleep(2)
    #Depot_End.click()

    asset_license_plate =context.browser.find_element(By.XPATH, xpaths.ASSET_LICENSE_PLATE)
    asset_license_plate.send_keys(Keys.CONTROL + "a")
    asset_license_plate.send_keys(Keys.DELETE)
    asset_license_plate.send_keys(License_Plate)
 #  asset_vehicle_manufacturer.keys(Keys.TAB)
    time.sleep(1)

    status_active =context.browser.find_element(By.XPATH,xpaths.ASSET_STATUS_ACTIVE)
    time.sleep(1)
    status_active.click()

    status_inactive =context.browser.find_element(By.XPATH,xpaths.ASSET_STATUS_INACTIVE)
    time.sleep(1)
    status_inactive.click()

    asset_save_button =context.browser.find_element(By.XPATH, xpaths.ASSET_SAVE_BUTTON)
    time.sleep(1)
    asset_save_button.click()
    time.sleep(5)

   
@then('User should be able to edit all the changes in asset and see the toast message as "Updated asset Successfully"')
def step_impl(context):
    
    success_message = context.browser.find_element(By.XPATH, xpaths.TOAST_ALERT)
    assert success_message.text == "Success"
    time.sleep(1)

#UPLOAD FILE  

@when('User click on Upload file and Download Vehicle Template file then clicks on the click or drag option to upload the file and import it')
def step_impl(context):
    upload_file_button=context.browser.find_element(By.XPATH, xpaths.ASSET_UPLOAD_FILE_BUTTON)
    upload_file_button.click()
    time.sleep(1)

    download_file_button=context.browser.find_element(By.XPATH, xpaths.ASSET_DOWNLOAD_FILE_BUTTON)
    download_file_button.click()
    time.sleep(1)

     # get the file path with current working directory
   #  directory = os.getcwd()
   #  bulk_upload_file_name = 'vehicle_vehicles_template (new).csv'
   #  file_path = os.path.join(directory, bulk_upload_file_name)

   #  file_input = context.browser.find_element(By.CSS_SELECTOR, "input[type='file']")
   #  file_input.send_keys(file_path)

  

    click_option=context.browser.find_element(By.XPATH, xpaths.ASSET_CLICK_OPTION)
    click_option.click()
    element = context.browser.find_element(By.ID,"dropzone-file")
    element.send_keys("C:/Users/hp/Downloads/vehicle_vehicles_template (new) (1).csv")
    time.sleep(1)
    
    import_csv_file =context.browser.find_element(By.XPATH, xpaths.ASSET_IMPORT_OPTION)
    import_csv_file.click()
    time.sleep(5)

    
@then('User should be able to see the success message as "Uploaded Successfully"')  
def step_impl(context):
   success_message = context.browser.find_element(By.XPATH, xpaths.TOAST_ALERT)
   assert success_message.text == "Success"
   time.sleep(1)

   
@when('User clicks on the block/unblock icon in asset page')
def step_impl(context):
    block_icon = context.browser.find_element(By.XPATH, xpaths.ASSET_BLOCK_ICON_BUTTON)
    block_icon.click()
    time.sleep(2)
    block_popup_message = context.browser.find_element(By.XPATH, xpaths.ASSET_BLOCK_POPUP_MESSEGE)
    block_popup_message.click()
    time.sleep(5)
    
@then('User able to activate/deactivate the asset')  
def step_impl(context):
   success_message = context.browser.find_element(By.XPATH, xpaths.TOAST_ALERT)
   assert success_message.text == "Success"
   time.sleep(1)

