Feature: SauceDemo Data Driven Login

    Scenario Outline: Login using different credentials

        Given I am on the SauceDemo login page
        When I enter username "<username>"
        And I enter password "<password>"
        And I click the login button
        Then the login result should be "<result>"

        Examples:
            |   username      |  password       |   result      |
            |   standard_user |  secret_sauce   |   success     |
            |   wrong_user    |  wrong_password |   error       |
            |   standard_user |  wrong_password |   error       |