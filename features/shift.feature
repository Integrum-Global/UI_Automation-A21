Feature: Accesing the Shift page of a21-dev Web Application

I want to access Shift web application page

# 1. Visibility Column
Scenario: Testing total visibility column of Shift in the listing page
Given I am on the Shift page of a21-dev web application
When User clicks on the Total visibility column to unchecks/checks the visibility status of the shift
Then User should be able to see the results of total visibility column while checking/unchecking the shift

# 2. Creating A Shift
Scenario: Create a new Shift
Given  I am on the Shift page of a21-dev web application
When User clicks add shift it takes to the shift page and enters the value Shift name as "Evening Shift", date filter by "filter_condition" and inputs "month_year" as MM-YYYY and "date" as DD,  StartWorkTime as "06:00", EndWorkTime as "12:00", BreakTimeStart as "10:00", BreakTimeEnd as "10:30" and Duration as "30" in the shift page 
      | start_date_month_year | end_date_month_year  | start_date_date       | end_date_date   |
      | February 2024         | March 2024            |                    1 |                1|
Then User able to create the Shift

# 3. Create a Shift with same details
Scenario: Create a new Shift with same details
Given  I am on the Shift page of a21-dev web application
When User clicks add shift for enter same details it takes to the shift page and enters the value Shift name as "Evening Shift", date filter by "filter_condition" and inputs "month_year" as MM-YYYY and "date" as DD,  StartWorkTime as "06:00", EndWorkTime as "12:00", BreakTimeStart as "10:00", BreakTimeEnd as "10:30" and Duration as "30" in the shift page 
      | start_date_month_year | end_date_month_year  | start_date_date       | end_date_date   |
      | February 2024         | March 2024           |                     1 |                1|
Then User should see the error message in the shift

# 4. Search Option
Scenario: Testing search option of Shift in the listing page
Given I am on the Shift page of a21-dev web application
When For checking search option user clicks add shift it takes to the shift page and enters the value Shift name as "Night Shift", date filter by "filter_condition" and inputs "month_year" as MM-YYYY and "date" as DD,  StartWorkTime as "10:00", EndWorkTime as "05:00", BreakTimeStart as "12:00", BreakTimeEnd as "12:30" and Duration as "30" in the shift page 
      | start_date_month_year | end_date_month_year  | start_date_date       | end_date_date   |
      | February 2024         | March 2024            |                    5 |                8|
And User clicks search to enters the value name as "Night Shift" in the shift page
Then User should see the created Shift in the listing page

# 5. Check search option giving wrong details
Scenario: Testing search option of Shift in the listing page
Given I am on the Shift page of a21-dev web application
When User clicks search option to enters the value name as "Day" in the shift page
Then User should see the error message like "Sorry" in the listing page

# 6. Creating Shift with mandotary details
Scenario: Can user create without filling the mandatory fields
Given I am on the Shift page of a21-dev web application
When User clicks add shift it takes to the add shift page and enters the value Shift name as "", StartDate as "" EndDate as "", StartWorkTime as "", EndWorkTime as "", BreakTimeStart as "", BreakTimeEnd as "" and Duration as "" in the shift page
Then User see the error message like "Required" in the shift

# 7. Edit changes in Shift
Scenario: Update changes in Shift
Given I am on the Shift page of a21-dev web application
When For edit the Shift user clicks add shift it takes to the shift page and enters the value Shift name as "Noon", date filter by "filter_condition" and inputs "month_year" as MM-YYYY and "date" as DD,  StartWorkTime as "08:00", EndWorkTime as "12:00", BreakTimeStart as "10:00", BreakTimeEnd as "10:30" and Duration as "30" in the shift page 
      | start_date_month_year | end_date_month_year  | start_date_date       | end_date_date   |
      | March 2024            | April 2024            |                    9 |                1|
And User clicks pencil icon it takes to edit shift and enters the value name as "SHIFT", date filter by "filter_condition" and inputs "month_year" as MM-YYYY and "date" as DD, StartDate as "February 5, 2024" EndDate as "March 11, 2024", StartWorkTime as "07:00", EndWorkTime as "01:00", BreakTimeStart as "11:00", BreakTimeEnd as "11:30" and Duration as "30" in the shift
                   | start_date_month_year | end_date_month_year  | start_date_date       | end_date_date   |
                   | February 2024         | March 2024           |                     1 |                1|
Then User shud edit the changes in the Shift

# 8. Delete the Shift
Scenario: Delete the Shift in a21-dev
Given  I am on the Shift page of a21-dev web application
When For delete the Shift user clicks add shift it takes to the shift page and enters the value Shift name as "XYZ", date filter by "filter_condition" and inputs "month_year" as MM-YYYY and "date" as DD,  StartWorkTime as "06:00", EndWorkTime as "12:00", BreakTimeStart as "10:00", BreakTimeEnd as "10:30" and Duration as "30" in the shift page 
      | start_date_month_year | end_date_month_year  | start_date_date       | end_date_date   |
      | February 2024         | March 2024            |                    1 |                1|
And User click trash icon in Shift page a21-dev web application 
Then User delete the Shift