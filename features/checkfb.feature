Feature: Check facebook

  Scenario: Open website and register with new facebook.
    Given I open website
    Then I click login facebook
    Then You sign up successful

#  Scenario: Open website and register with already signed up facebook.
#    Given I open website
#    Then I click login facebook
#    Then I have already signed up facebook.