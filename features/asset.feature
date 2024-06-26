Feature: Accesing the Asset page of a21-dev Web Application

I want to access asset web application page

@Scenario1
#1. Check visibility column
Scenario: Testing Total visibility column of asset in the Listing page
Given I am on the asset page of a21-dev web application
When User clicks on the Total visibility column to unchecks/checks the visibility status of the asset
Then User should be able to see the results of total visibility column while checking/unchecking the asset

@Scenario2
#2. Create new Asset
Scenario: Create a new asset 
Given  I am on the asset page of a21-dev web application
When  User clicks on the add asset it takes to add asset page and enters the asset Vehicle Type, License Plate as "TEST 107", Depot Start and Depot End
Then  User should be able to create the asset and see the toast message as "Created asset Successfully"

@Scenario3
#3. Checking Search Option 
Scenario: Testing the presence of the created asset by using searchfield
Given  I am on the asset page of a21-dev web application
When User clicks on the add asset it takes to add asset page and enters the asset Vehicle Type, License Plate as "TEST 108", Depot Start and Depot End
And User clicks on the searchfield and enters the created asset License Plate as "TEST 108"
Then User should be able to see the results of Created asset License Plate as "TEST 108"

@Scenario4
#4. Check search option giving wrong details
Scenario: Searching for the wrong asset name through the search field
Given I am on the asset page of a21-dev web application
When User clicks on the searchfield and enters the wrong asset License Plate as "TN63BW3636"
Then User should be able to see the error message as "No assets found" in the asset page

@Scenario5
#5. Creating Asset with Same Details and unique name
Scenario: Creating Asset with same details and unique name
Given  I am on the asset page of a21-dev web application
When User clicks on the add asset it takes to add asset page and enters the asset Vehicle Type, License Plate as "TEST 109", Depot Start and Depot End
And  User clicks on the add asset and enters the asset with same details the Vehicle Type, License Plate as "TEST 109", Depot Start and Depot End
Then  User should be able to see the error message as "Vehicle type Name already exists"

@Scenario6
#6. Creating Asset with mandotary details
Scenario: Can user create a asset without completing the mandatory fields
Given  I am on the asset page of a21-dev web application
When  User clicks add asset and leave the asset fields as empty 
Then User see the error message like "Required" in asset

@Scenario7
#7. Edit changes in Asset
Scenario: Update all the changes in asset 
Given  I am on the asset page of a21-dev web application
When User clicks on the add asset it takes to add asset page and enters the asset Vehicle Type, License Plate as "TEST 110", Depot Start and Depot End
And User clicks pencil icon it takes to edit asset page and enters the asset Vehicle Type, License Plate as "TEST 111", Depot Start and Depot End
Then User should be able to edit all the changes in asset and see the toast message as "Updated asset Successfully" 

@Scenario8
#Upload vehicle Template

Scenario: Upload Vehicle Template file in the Asset
Given  I am on the asset page of a21-dev web application
When User click on Upload file and Download Vehicle Template file then clicks on the click or drag option to upload the file and import it
Then User should be able to see the success message as "Uploaded Successfully"

@Scenario9
#9. Block/Unblock the Asset
Scenario: Block/unblock the asset in asset page
Given  I am on the asset page of a21-dev web application
When User clicks on the add asset it takes to add asset page and enters the asset Vehicle Type, License Plate as "TEST 112", Depot Start and Depot End 
And User clicks on the block/unblock icon in asset page
Then User able to activate/deactivate the asset

