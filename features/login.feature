Feature: Login into integrum mobility 

  As a user
  I want to login into integrum mobility web application
  So that I can access the application
  
Scenario: Login into integrum mobility web application with the user credentials
Given I am on the login page of integrum mobility web application
When I enter the username as "parimal.nakrani@integrum.global" and password "123456"
Then I should be able to login into the application


Scenario: Login into integrum mobility web application with the invalid user credentials
Given I am on the login page of integrum mobility web application
When I enter the username as "gokul.marish@gmail.com" and password "123456"
Then I should see error message