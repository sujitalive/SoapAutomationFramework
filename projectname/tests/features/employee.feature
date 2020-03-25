Feature: example

#  Scenario: test 1st scenario
#    Given A valid payload
#      |   method    | var1  | var2 |
#      | AddInteger  |   2   |   3  |
#      | AddInteger  |   4   |   5  |
#      | AddInteger  |   10   |   10  |
#    When I call AddInteger
#    Then The response should be OK



#      |   method    | var1  | var2 |var3 |
#      | AddInteger  |   2   |   3  |2    |
#      | AddInteger  |   4   |   5  |2    |


  @prod
    Scenario: test 1st scenario
    Given A valid payload
      |   method    | var1  | var2 |
      | DivideInteger  |   6   |   3  |
      | DivideInteger  |   10   |   5  |
      | DivideInteger  |   10   |   10  |
    When I call the service
    Then The response should be OK

    @qa
  Scenario: test 1st scenario
    Given A valid payload
      |   method    | var1  |
      | FindPerson  |   1   |
      | FindPerson  |   2   |
      | FindPerson  |   3   |
    When I call the service
    Then The response should be OK