Feature: Accesing the User Management page of a21-dev Web Application

I want to access User Management web application page


Scenario: Testing Total visibility column of User Management in the Listing page
Given I am on the User Management Page of a21-dev web application
When User clicks on the Total visibility column to unchecks/checks the visibility status of the User Management
Then User should be able to see the results of total visibility column while checking/unchecking the User Management

Scenario: Testing search option of User Management in the Listing page
Given  I am on the User Management Page of a21-dev web application
When User clicks on the search option and enters the Name as "Gokul" in user management 
Then User should be able to see the results of the search option in User Management

Scenario: Testing search option of User Management in the Listing page
Given  I am on the User Management Page of a21-dev web application
When User clicks on the search option and enters the Name as "XXXXX" in user management 
Then User should be able to see the error message as "No User found" in the User Management page

@wip
Scenario: Update all the changes in User Management
Given I am on the User Management Page of a21-dev web application
When User clicks on the pencil icon it takes to edit User Management page and enters the User Management Roles, Name as "Gokul", Email as "test@gmail.com", Phone Number as "+919876543210", date filter by "filter_condition" and inputs "month_year" as MM-YYYY and "date" as DD, Status
      | contract_start_date_month_year | contract_end_date_month_year  | contract_start_date_date       | contract_end_date_date     |
      | Jun 2021                       | Jun 2021                       |                              11|                        20|
Then User should be able to edit all the changes in User Management and see the toast message as "Success"

Scenario: Update phone number and status in User Management
Given I am on the User Management Page of a21-dev web application
When User clicks on the pencil icon it takes to edit User Management page and enters the User Management Roles, Name as "Gokul", Email as "test@gmail.com", Thailand Phone Number as "+66987654321", date filter by "filter_condition" and inputs "month_year" as MM-YYYY and "date" as DD, Status
      | contract_start_date_month_year | contract_end_date_month_year  | contract_start_date_date       | contract_end_date_date   |
      | Jun 2021                       | Jun 2021                     |                                11|                        20|
Then User should be able to edit the phone Number and status in the User Management and see the toast message as "Success"

Scenario: Block and Unblock the User in User Management
Given I am on the User Management Page of a21-dev web application
When User clicks on the block/Unblock icon in User Management
Then User able to deactivate/activate the User in User Management