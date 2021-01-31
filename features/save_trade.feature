Feature: Save Trade
  This Feature verify the Save Trade Feature, which save a specific Trade in database
  Scenario: Save Trade
    Given a request url http://localhost:8000/trade/save/
    And a request json payload
      """
        {
            "right_side": [
                {
                    "name": "teste1",
                    "base_experience": 200,
                    "image": "url"
                },
                {
                    "name": "teste1",
                    "base_experience": 200,
                    "image": "url"
                }
            ],
            "left_side": [
                {
                    "name": "teste1",
                    "base_experience": 400,
                    "image": "url"
                }
            ],
            "result": "This trade is fair!"
        }
      """
    When the request sends POST
    Then the response status is OK
    And the response json matches
      """
        {
            "right_side": [
                {
                    "name": "teste1",
                    "base_experience": 200,
                    "image": "url"
                },
                {
                    "name": "teste1",
                    "base_experience": 200,
                    "image": "url"
                }
            ],
            "left_side": [
                {
                    "name": "teste1",
                    "base_experience": 400,
                    "image": "url"
                }
            ],
            "result": "This trade is fair!"
        }
      """
