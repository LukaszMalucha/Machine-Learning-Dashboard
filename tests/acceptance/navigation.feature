Feature: Test navigation between pages


  Scenario: Home can go to Classification
    Given I am on the homepage
    When I click on the "CLASSIFICATION" link
    Then I am on the classification page

  Scenario: Home can go to Clustering
    Given I am on the homepage
    When I click on the "CLUSTERING" link
    Then I am on the classification page

  Scenario: Home can go to Regression
    Given I am on the homepage
    When I click on the "REGRESSION" link
    Then I am on the regression page

  Scenario: Home can go to Add Template
    Given I am on the homepage
    When I click on the "ADD TEMPLATE" link
    Then I am on the add template page


  Scenario: Home can go to Login
    Given I am on the homepage
    When I click on the dropdown menu
    Given I wait for the dropdown to load
    When I click on the "Log In" dropdown link
    Then I am on the login page

  Scenario: Home can go to Logout
    Given I am on the homepage
    When I click on the dropdown menu
    Given I wait for the dropdown to load
    When I click on the "Log Out" dropdown link
    Then I am on the login page

  Scenario: Home can go to Signup
    Given I am on the homepage
    When I click on the dropdown menu
    Given I wait for the dropdown to load
    When I click on the "Sign In" dropdown link
    Then I am on the signup page

  Scenario: Home can go to Manage DB
    Given I am on the homepage
    When I click on the dropdown menu
    Given I wait for the dropdown to load
    When I click on the "Manage DB" dropdown link
    Then I am on the manage db page


