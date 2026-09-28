Feature: SauceDemo Login using Page Object Model

  Scenario Outline: Login using different credentials

    Given I am on the SauceDemo login page
    When I login using username "<username>" and password "<password>"
    Then the login result should be "<result>"

    Examples:
      | username       | password       | result  |
      | standard_user  | secret_sauce   | success |
      | wrong_user     | wrong_password | error   |
      | standard_user  | wrong_password | error   |