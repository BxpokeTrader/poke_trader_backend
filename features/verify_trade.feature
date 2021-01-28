Feature: Verify trade

  This feature verify if a pokemon trade is fair or not. That is, it verify if the both sides has equivalent "values"

  Scenario: Verify a fair trade
    Given that I have the same pokemon in both sides
    When I request to verify it
    Then the system returns "This trade is fair!"

  Scenario: Verify an unfair trade
    Given that I have a pokemon with high value in the right side and a simple pokemon in the left side
    When I request to verify it
    Then the system returns "This trade is unfair!"
