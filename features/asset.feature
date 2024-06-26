Feature: Accesing the Asset page of a21-dev Web Application

I want to access asset web application page

#Check visibility column 
Scenario: Testing Total visibility column of asset in the Listing page
Given I am on the asset page of a21-dev web application
When User clicks on the Total visibility column to unchecks/checks the visibility status of the asset
Then User should be able to see the results of total visibility column while checking/unchecking the asset

Scenario: Create a new asset 
Given  I am on the asset page of a21-dev web application
When  User clicks on the add asset it takes to add asset page and enters the asset Vehicle Manufacturer as "2023", Vehicle Model as "XX", Vehicle Type as " ", Vehicle Company as "NA", Register Number as"#27CK23", Depot Start, Depot End, License Plate as "TEST 107" and Status
Then  User should be able to create the asset and see the toast message as "Created asset Successfully"

#Check search option 
Scenario: Testing the presence of the created asset by using searchfield
Given  I am on the asset page of a21-dev web application
When User clicks on the searchfield and enters the created asset License Plate as "TEST 107"
Then User should be able to see the results of Created asset

Scenario: Searching for the wrong asset name through the search field
Given I am on the asset page of a21-dev web application
When User clicks on the searchfield and enters the wrong asset License Plate as "TN63BW3636"
Then User should be able to see the error message as "No assets found" in the asset page

#same details and unique details
Scenario: Creating Asset with same details and unique name
Given  I am on the asset page of a21-dev web application
When  User clicks on the add asset and enters the asset with same details the Vehicle Manufacturer as "2023", Vehicle Model as "XX", Vehicle Type as " ", Vehicle Company as "NA", Register Number as"#27CK23", Depot Start, Depot End, License Plate as "TESTING_3" and Status
And User enters the asset with unique details the Vehicle Manufacturer as "2024", Vehicle Model as "XXX", Vehicle Type as " ", Vehicle Company as "XXX", Register Number as"#27CK24", Depot Start, Depot End, License Plate as "TESTING_3" and Status
Then  User should be able to see the error message as "Vehicle type Name already exists"

#Create Asset without filling mandatory details
Scenario: Can user create a asset without completing the mandatory fields
Given  I am on the asset page of a21-dev web application
When  User clicks add asset and leave the asset fields empty the Vehicle Manufacturer as "", Vehicle Model as "", Vehicle Type as "", Vehicle Company as "", Register Number "", Deport Start, Depot End, License Plate "" and Status
Then User see the error message like "Required" in asset

#Edit some changes in asset
Scenario: Update all the changes in asset 
Given  I am on the asset page of a21-dev web application
When User clicks pencil icon it takes to edit asset page and enters the asset Vehicle Manufacturer as "NA", Vehicle Model as "NA", Vehicle Type as " ", Vehicle Company as "NA", Register Number as"NA", Depot Start, Depot End, License Plate as "NA" and Status
Then User should be able to edit all the changes in asset and see the toast message as "Updated asset Successfully" 

#Upload vehicle Template

Scenario: Upload Vehicle Template file in the Asset
Given  I am on the asset page of a21-dev web application
When User click on Upload file and Download Vehicle Template file then clicks on the click or drag option to upload the file and import it
Then User should be able to see the success message as "Uploaded Successfully"

#Block/unblock the asset
Scenario: Block/unblock the asset in asset page
Given  I am on the asset page of a21-dev web application
When User clicks on the block/unblock icon in asset page
Then User able to activate/deactivate the asset

