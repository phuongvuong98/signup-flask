Feature: Check website

  Scenario: Open website
    Given I open website
    Then I print the html

  Scenario: Open website and submit form with password and email is none
    Given I open website
    Then I submit form
    Then I print email error

  Scenario: Open website and submit form with email is none
    Given I open website
    Then I input password
    Then I submit form
    Then I print email error

  Scenario: Open website and submit form with password is none
    Given I open website
    Then I input email
    Then I submit form
    Then I print password error

  Scenario: Open website and submit form with email is incorrect
    Given I open website
    Then I input incorrect email
    Then I input password
    Then I submit form
    Then I print incorrect email error