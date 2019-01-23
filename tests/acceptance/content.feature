Feature: Test that page have correct content


  Scenario: Homepage has a correct title
    Given I am on the homepage
    Then There is a title shown on the page
    And The title tag has content "ML Dashboard"

  Scenario: Homepage has a table
    Given I am on the homepage
    Then I can see there is a table on the page

  Scenario: Homepage has a Github Repos
    Given I am on the homepage
    Then I can see there are Github Repos in the page

  Scenario: Signup page loads the form
   Given I am on the signup page
   Then I can see there is a signup form on the page

  Scenario: Login page loads the form
   Given I am on the login page
   Then I can see there is a login form on the page

  Scenario: Add Template page has a form
    Given I am on the add template page
    Then I can see there is an add template form on the page

  Scenario: Edit Template page has a form
    Given I am on the edit template page
    Then I can see there is an edit template form on the page

  Scenario: Manage DB page has an add algorithm type form
    Given I am on the manage db page
    Then I can see there four forms displayed on the page

  Scenario: Classification page has three algorithm choices
    Given I am on the classification page
    Then I can see there are three classification algorithm choices

  Scenario: Clustering page has two algorithm choices
    Given I am on the clustering page
    Then I can see there are two clustering algorithm choices

  Scenario: Regression page has three algorithm choices
    Given I am on the regression page
    Then I can see there are three regression algorithm choices

  Scenario: Naive Bayes displays plot and Accuracy
    Given I am on the classification page
    When I scroll to the bottom of the page
    Given I wait for the classification page to load
    When I click on the "NAIVE BAYES" navigation link
    Given I wait for the plot to load
    Then I can see there is a plot on the page







