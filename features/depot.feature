Feature: Accesing the Depot page of a21-dev Web Application

I want to access Depot web application page

Scenario: Testing total visibility column of depot in the listing page
Given I am on the depot page of a21-dev web application
When User clicks on the Total visibility column to unchecks/checks the visibility status of the depot
Then User should be able to see the results of total visibility column while checking/unchecking the depot

Scenario: Create a new depot
Given  I am on the depot page of a21-dev web application
When  User clicks add depot it takes to add depot and enters the add depot name as "A21-dev", description as "House", lat as "1.3521" , long as "103.8198" , address as "Singapore" in the depot page
Then  User able to create the depot

Scenario: Testing search name of depot in the Listing page
Given I am on the depot page of a21-dev web application
When User clicks search to enters the value name as "Integrum" in the depot page
Then User should see the result in the depot page

Scenario: Testing search name of depot in the Listing page
Given I am on the depot page of a21-dev web application
When User clicks search to enters the value name as "mobility" in the depot
Then User should see the error message in the depot page

Scenario: Create a new depot with same details
Given I am on the depot page of a21-dev web application
When User clicks add depot it takes to add depot and enters the add depot name as "A21-dev", description as "House", lat as "1.3521" , long as "103.8198" , address as "Singapore" in the depot
#And User enters the add depot name as "Integrum", description as "House", lat as "1.3521" , long as "103.8198" , address as "Singapore" in the depot
Then User see the error message like Depot Already Exists in the depot page

Scenario: Can user create without filling the mandatory fields
Given I am on the depot page of a21-dev web application
When User clicks add depot it takes to add depot page and enters the add depot name as "", description as "", lat as "" , long as "" , address as "" in the depot
Then User should see the error message like "Required" in the depot page

Scenario: Update some changes in depot
Given I am on the depot page of a21-dev web application
When User clicks pencil icon it takes to edit depot and enters the depot name as "A21", description as "A21", lat as "1.3521" , long as "103.8198" , address as "Singapore" in the depot
Then User able to edit the changes in the depot

Scenario: Delete the depot in a21-dev
Given  I am on the depot page of a21-dev web application
When User click trash icon in depot page 
Then User delete the depot 