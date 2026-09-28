Feature: SauceDemo Login

  Scenario: Successful login with valid credentials

    Given I am on the SauceDemo login page
    When I enter the valid username
    And I enter the valid password
    And I click the login button
    Then I should be redirected to the inventory page