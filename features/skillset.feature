Feature: Accesing the Skillset page of a21-dev Web Application

I want to access Skillset web application page

#Check visibility column 
Scenario: Testing Total visibility column of skillset in the Listing page
Given I am on the Skillset Page of a21-dev web application
When User clicks on the Total visibility column to unchecks/checks the visibility status of the skillset
Then User should be able to see the results of total visibility column while checking/unchecking the skillset

#Create new skillset
Scenario:Create a new Skillset
Given I am on the Skillset Page of a21-dev web application
When User clicks on the add Skillset it takes to add Skillset page and enters the Skillset Name as "test3", Category as "XX", Sub category as "Car", Remarks as "NA"
Then User should be able to create the Skillset and see the toast message as "Created Skillset Successfully"

#Check the created skillset through search option
Scenario: Testing the presence of the created skillset by using searchfield
Given I am on the Skillset Page of a21-dev web application
When User clicks on the searchfield and enters the created skillset Name as "test3"
Then User should be able to see the results of Created Skillset

Scenario: Searching for the wrong skillset name through the search field
Given  I am on the Skillset Page of a21-dev web application
When  User clicks on the searchfield and enters the wrong skillset Name as "XXXX"
Then User should be able to see the error message as "No skillsets found" in the skillset page

#Create skillset with Same Details and unique name
Scenario: Creating Skillset with same details and unique Name
Given I am on the Skillset Page of a21-dev web application
When User clicks on add Skillset and enters the Skillset with same details the Name as "test3", Category as "XX", Sub category as "car", Remarks as "NA"
#And User enters the Skillset with unique details the Name as "Test", Category as "XXX", Sub category as "XXX", Remarks as "XXX"
Then User should be able to see the error message as "skillset already exist in database"

#Create skillset without filling mandatory details
Scenario: Can user create a skillset without completing the mandatory fields
Given I am on the Skillset Page of a21-dev web application
When User clicks add Skillset and leave the Skillset fields empty the Name as " ", Category as " ", Sub category as " ", Remarks
Then User should be able to see the error message as "Required" in Add skillset page

#Edit changes in skillset
Scenario: Update all the changes in the Skillset 
Given I am on the Skillset Page of a21-dev web application
When User clicks on pencil icon it takes to edit Skillset page and enters the Skillset Name as "test2 ", Category as "NA", Sub category as "NA", Remarks as "NA"
Then User should be able to edit all the changes in skillset and see the toast message as "Updated Skill Set Successfully"

#Delete the skillset
Scenario: Delete the Skillset
Given I am on the Skillset Page of a21-dev web application
When User clicks on the delete icon in skillset page
Then User should be able to delete the Skillset and see the toast message as "Deleted Skill Set Successfully"
