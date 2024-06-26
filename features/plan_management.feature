Feature: Accesing the Plan Management page of a21-dev Web Application

I want to access Plan Management web application page

# 1. Visibility Column
Scenario: Testing Total visibility column of Plan Management in the Listing page
Given I am on the Plan Management page of a21-dev web application
When User clicks on the Total visibility column to unchecks/checks the visibility status of the Plan Management
Then User should be able to see the results of total visibility column while checking/unchecking the Plan Management

# 2. Creating A Plan
Scenario: Create a new plan
Given I am on the Plan Management page of a21-dev web application
When User clicks on the add Plan it takes to add Plan page and enters the Plan Name as "SkillTest", Description as "N/A", date filter by "filter_condition" and inputs "month_year" as MM-YYYY and "date" as DD, Depot Start and Depot End
          | start_date_month_year  |           start_date_date | 
          | July 2023              |                        22 |
Then User should be able to create the Plan and see the toast message as "Created plan Successfully"


# 3. Search Option 
Scenario: Testing the presence of the created plan by using searchfield
Given  I am on the Plan Management page of a21-dev web application
When  For checking search option user clicks on the add Plan it takes to add Plan page and enters the Plan Name as "CheckTest", Description as "N/A", date filter by "filter_condition" and inputs "month_year" as MM-YYYY and "date" as DD, Depot Start and Depot End
          | start_date_month_year  |           start_date_date | 
          | July 2023              |                        22 |
And User clicks on the searchfield and enters the created plan Name as "CheckTest"
Then User should be able to see the results of Created plan

# 4. Check search option giving wrong details
Scenario: Searching for the wrong plan name through the search field
Given I am on the Plan Management page of a21-dev web application
When User clicks on the searchfield and enters the wrong plan as "XXXX" 
Then User should be able to see the error message as "No plan found" in the plan Management page

# 5. Creating plan with mandotary details
Scenario: Can user create a Plan without completing the mandatory fields
Given  I am on the Plan Management page of a21-dev web application
When  User clicks add plan and leave the plan fields empty
Then User see the error message like "Required" in create plan page

#6. Edit changes in Plan
Scenario: Update all the changes in Plan 
Given I am on the Plan Management page of a21-dev web application
When For Edit Plan user clicks on the add Plan it takes to add Plan page and enters the Plan Name as "ErrorTest", Description as "N/A", date filter by "filter_condition" and inputs "month_year" as MM-YYYY and "date" as DD, Depot Start and Depot End
          | start_date_month_year  |           start_date_date | 
          | July 2023              |                        22 |
And User clicks pencil icon it takes to edit plan page and enters the plan Name as "Testing_3", Description as "XX", Date, Depot Start and Depot End
Then User should be able to edit all the changes in plan and see the toast message as "Updated plan Successfully" 

#7. Delete the plan
Scenario: Delete the plan
Given I am on the Plan Management page of a21-dev web application
When For Delete Plan user clicks on the add Plan it takes to add Plan page and enters the Plan Name as "MobileTest", Description as "N/A", date filter by "filter_condition" and inputs "month_year" as MM-YYYY and "date" as DD, Depot Start and Depot End
          | start_date_month_year  |           start_date_date | 
          | July 2023              |                        22 | 
And User clicks on the trash icon in plan page
Then User should be able to delete the plan and see the toast message as "Deleted plan Successfully"

