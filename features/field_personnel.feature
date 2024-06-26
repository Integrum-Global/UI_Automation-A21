Feature: Accesing the Field Personnel page of a21-dev Web Application

I want to access Field Personnel web application page

#Check visibility column 
Scenario: Testing Total visibility column of Field Personnel in the Listing page
Given I am on the Field Personnel Page of a21-dev web application
When User clicks on the Total visibility column to unchecks/checks the visibility status of the Field Personnel
Then User should be able to see the results of total visibility column while checking/unchecking the Field Personnel

#Create new Field Personnel
Scenario:Create a new Field Personnel
Given I am on the Field Personnel Page of a21-dev web application
When User clicks on the add Field Personnel it takes to add Field Personnel page and enters the Field Personnel Name as "test3", Contact Number as "+66795863212", Email as "test2000@gmail.com", Skillset, Zones, date filter by "filter_condition" and inputs "month_year" as MM-YYYY and "date" as DD and Status
      | contract_start_date_month_year | contract_end_date_month_year  | contract_start_date_date       | contract_end_date_date   |
      | July 2024                      | July 2024                     |                               1|                        15|
Then User should be able to create the Field Personnel and see the toast message as "Success"

#Check the created Field Personnel through search option
Scenario:Testing the presence of the created skillset by using searchfield Field Personnel
Given I am on the Field Personnel Page of a21-dev web application
When User clicks on the searchfield and enters the created Field Personnel Name as "Gokul"
Then User should be able to see the results of Created Field Personnel

Scenario: Searching for the wrong Field Personnel name through the search field
Given  I am on the Field Personnel Page of a21-dev web application
When User clicks on the searchfield and enters the wrong Field Personnel Name as "pluto" 
Then User should be able to see the error message as "No field personnels found" in the Field Personnel page

 #Create Field Personnel with Same Details and unique name
 
 Scenario: Creating Field Personnel with same details and unique name
 Given I am on the Field Personnel Page of a21-dev web application
 When User clicks on the add Field Personnel it takes to add Field Personnel page and enters the Field Personnel Name as "test3", Contact Number as "+66795863212", Email as "test2000@gmail.com", Skillset, Zones, date filter by "filter_condition" and inputs "month_year" as MM-YYYY and "date" as DD and Status
      | contract_start_date_month_year | contract_end_date_month_year  | contract_start_date_date       | contract_end_date_date   |
      | July 2024                      | July 2024                     |                               1|                        15|
#  And User enters the Field Personnel with unique details the Name as "Gokul", Contact Number as "7904586327", Email as "test2000@gmail.com", Skillset, Zones, date filter by "filter_condition" and inputs "month_year" as MM-YYYY and "date" as DD, Shift and Status
#       | contract_start_date_month_year | contract_end_date_month_year  | contract_start_date_date       | contract_end_date_date   |
#       | May 2023                       | May 2023                      |                              23|                        27|
 Then User should be able to see the error message as "User already exists"

#Create Field Personnel without filling mandatory details
Scenario: Can user create a Field Personnel without completing the mandatory fields
Given I am on the Field Personnel Page of a21-dev web application
When User clicks on the add Skillset and leave the Field Personnel fields empty the Name as "", Contact Number as "", Email as "", Skillset, Zones, Contract Start Date, Contract End Date, Shift and Status
Then User should be able to see the error message as "Required" in Add Field Personnel page

#Edit changes in Field Personnel
 Scenario: Update all the changes in Field Personnel 
 Given I am on the Field Personnel Page of a21-dev web application
When User clicks on the add Field Personnel it takes to add Field Personnel page and enters the Field Personnel Name as "test3", Contact Number as "+66795863212", Email as "test2000@gmail.com", Skillset, Zones, date filter by "filter_condition" and inputs "month_year" as MM-YYYY and "date" as DD and Status
      | contract_start_date_month_year | contract_end_date_month_year  | contract_start_date_date       | contract_end_date_date   |
      | July 2024                      | July 2024                     |                               1|                        15|
 Then User should be able to edit all the changes in Field Personnel and see the toast message as "Success"

 Scenario: Update phone number and status in Field Personnel 
 Given I am on the Field Personnel Page of a21-dev web application
When User clicks on the add Field Personnel it takes to add Field Personnel page and enters the Field Personnel Name as "test3", Contact Number as "+66795863212", Email as "test2000@gmail.com", Skillset, Zones, date filter by "filter_condition" and inputs "month_year" as MM-YYYY and "date" as DD and Status
      | contract_start_date_month_year | contract_end_date_month_year  | contract_start_date_date       | contract_end_date_date   |
      | July 2024                      | July 2024                     |                               1|                        15|
 Then User should be able to edit the phone Number and status in the Field Personnel and see the toast message as "Success"

#Block/Unblock the Field Personnel
Scenario: Block/Unblock the Field Personnel
Given I am on the Field Personnel Page of a21-dev web application
When User clicks on the block/unblock icon in Field Personnel page
Then User able to activate/deactivate the Field Personnel