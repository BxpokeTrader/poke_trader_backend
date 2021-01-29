Feature: Verify trade

  This feature verify if a pokemon trade is fair or not. That is, it verify if the both sides has equivalent "values"

  Scenario: Verify a fair trade
    Given a request url http://localhost:8000/trade/verify/
    And a request json payload
      """
        {"right_side": [
          {"name": "Charmander", "base_expecience": 100
        }
          ], "left_side": [
              {"name": "Charmander", "base_expecience": 100
              }
          ], "result": ""
        }
      """
    When the request sends POST
    Then the response status is OK
    And the response json matches
      """
        {
            "right_side": [
                {
                    "name": "Charmander",
                    "base_expecience": 100
                }
            ],
            "left_side": [
                {
                    "name": "Charmander",
                    "base_expecience": 100
                }
            ],
            "result": "This trade is fair!"
        }
      """

  Scenario: Verify an unfair trade
    Given a request url http://localhost:8000/trade/verify/
    And a request json payload
      """
        {
           "right_side":[
              {
                 "name":"Charmander",
                 "base_expecience":100
              },
              {
                 "name":"Charmander",
                 "base_expecience":100
              }
           ],
           "left_side":[
              {
                 "name":"Charmander",
                 "base_expecience":100
              }
           ],
           "result":""
        }
      """
    When the request sends POST
    Then the response status is OK
    And the response json matches
      """
        {
           "right_side":[
              {
                 "name":"teste1",
                 "base_expecience":200
              }
           ],
           "left_side":[
              {
                 "name":"teste1",
                 "base_expecience":200
              },
              {
                 "name":"teste1",
                 "base_expecience":200
              }
           ],
           "result":""
        }
      """
