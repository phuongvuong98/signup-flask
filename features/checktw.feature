Feature: Check twitter

  Scenario: Open website and register with new twitter.
    Given I open website
    Then I click login twitter
    Then You sign up successful

#    Scenario: Open website and register with already signed up twitter
#    Given I open website
#    Then I click login twitter
#    Then I have already signed up twitter.