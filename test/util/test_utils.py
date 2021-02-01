from trade.models import Trade, Pokemon


def create_default_trade():
    pokemon1 = {'name': 'pikachu', 'base_experience': 112, 'image': 'url'}
    pokemon2 = {'name': 'charmander', 'base_experience': 62, 'image': 'url'}
    trade = Trade()
    trade.right_side = [pokemon1, pokemon2]
    trade.left_side = [pokemon1, pokemon2]
    trade.result = trade.is_fair()

    return trade


def create_unfair_trade():
    pokemon1 = {'name': 'pikachu', 'base_experience': 112, 'image': 'url'}
    pokemon2 = {'name': 'charmander', 'base_experience': 62, 'image': 'url'}
    trade = Trade()
    trade.right_side = [pokemon1]
    trade.left_side = [pokemon2]
    trade.result = trade.is_fair()

    return trade


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if 'https://pokeapi.co/api/v2/pokemon/' in args[0]:
        return MockResponse({'location_area_encounters': ""}, 200)
    else:
        return MockResponse([1, 2, 3], 200)
