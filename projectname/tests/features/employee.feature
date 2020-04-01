#@beforedeployement
#@afterdeployement
Feature: example
  @prod
    Scenario: test 1st scenario
    Given A valid payload
      |scenario name|   method        | var1    | var2  |
      |odd          | DivideInteger   |   6     |   3   |
      |even         | DivideInteger   |   10    |   5   |
      |max          | DivideInteger   |   10    |   10  |
    When I call the service
    Then The response should be OK

