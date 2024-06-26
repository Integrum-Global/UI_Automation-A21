Feature: Accesing the Items page of a21-dev Web Application

I want to access Items web application page

Scenario: Testing total visibility column of Items in the listing page
Given I am on the Items page of a21-dev web application
When User clicks on the Total visibility column to unchecks/checks the visibility status of the items
Then User should be able to see the results of total visibility column while checking/unchecking the items

Scenario: Create a new Items
Given  I am on the Items page of a21-dev web application
When User clicks add items it takes to the items page and enters the value Name as "3 Roses", Description as "Tea", Category as "Liquid", SKUID as 10000568, Weight as 15, Status as "Active" and Inner Pack as 5 in the items page
Then User shud able to create the Items

Scenario: Testing search name of items in the Listing page
Given I am on the items page of a21-dev web application
When User clicks search to enters the value name as "3 Roses" in the items page
Then User see the created items in the listing page

Scenario: Testing search name of items in the Listing page
Given I am on the items page of a21-dev web application
When User clicks search to enters the value name as "Coffee" in the items
Then User see the error message like "Sorry" in the items listing page

Scenario: Create a new Items with same details
Given  I am on the Items page of a21-dev web application
When User clicks add items it takes to the items page and enters the value Name as "3 Roses", Description as "Tea", Category as "Liquid", SKUID as 10000568, Weight as 15, Status as "Active" and Inner Pack as 5 in the items
And User enters the value Name as "3 Roses", Description as "Natural", Category as "Powder", SKUID as 10000589, Weight as 10, Status as "Active" and Inner Pack as 7 in the items
Then User shud see error message like "Item with the same name or SKU already exists" in the items page

Scenario: Create a new Items without filling mandatory details
Given  I am on the Items page of a21-dev web application
When User clicks add items it takes to the items page and enters the value Name as "", Description as "", Category as "", SKUID as , Weight as , Status as "" and Inner Pack as in the items
Then User shud able to see the error message like "Required" in the items

# Scenario: Upload Vehicle Template file in the Asset
# Given I am on the Items page of a21-dev web application
# When User click on Upload file and Download SQL Template in items page then clicks on the click or drag option to upload the file and import it
#Then User should be able to see the success message as "Uploaded Successfully" in the items page


Scenario: Update some changes in items page
Given  I am on the Items page of a21-dev web application
When User clicks pencil icon in items it takes to the items page and enters the value Name as "Milk", Description as "Powder", Category as "Liquid", SKUID as 100005515, Weight as 10, Status as "Active" and Inner Pack as 7 in the items
Then User shud able to update the changes in the Items

Scenario: Delete the items in a21-dev
Given  I am on the items page of a21-dev web application
When User click trash icon in the items
Then User able to delete the items page 