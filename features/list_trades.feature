Feature: List Historical Trades
  Scenario: List without previous trades
    Given a request url http://localhost:8000/trade/
    When the request sends GET
    Then the response status is OK
    And the response json matches
      """
      {
        "trades": [
        ]
      }
      """
  Scenario: List trades
    Given that 2 trades are already saved
    And a request url http://localhost:8000/trade/
    When the request sends GET
    Then the response status is OK
    And the response json matches
      """
         {
            "trades": [
                {
                    "right_side": [
                        {
                            "name": "pikachu",
                            "base_experience": 112,
                            "image": "url"
                        },
                        {
                            "name": "charmander",
                            "base_experience": 62,
                            "image": "url"
                        }
                    ],
                    "left_side": [
                        {
                            "name": "pikachu",
                            "base_experience": 112,
                            "image": "url"
                        },
                        {
                            "name": "charmander",
                            "base_experience": 62,
                            "image": "url"
                        }
                    ],
                    "result": "This trade is unfair!"
                },
                {
                    "right_side": [
                        {
                            "name": "pikachu",
                            "base_experience": 112,
                            "image": "url"
                        },
                        {
                            "name": "charmander",
                            "base_experience": 62,
                            "image": "url"
                        }
                    ],
                    "left_side": [
                        {
                            "name": "pikachu",
                            "base_experience": 112,
                            "image": "url"
                        },
                        {
                            "name": "charmander",
                            "base_experience": 62,
                            "image": "url"
                        }
                    ],
                    "result": "This trade is unfair!"
                }
            ]
        }
      """