Feature: example

  @positive
  Scenario: test 1st scenario
    When I call GET http://dummy.restapiexample.com/api/v1/employees
    Then The response should be OK


#  Scenario: test 1st scenario
#    Given A valid payload to create an employee
#    When I call POST http://dummy.restapiexample.com/api/v1/create
#    Then The response should be OK