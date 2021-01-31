from trade.models import Trade, Pokemon


def create_default_trade():
    pokemon1 = {'name': 'Pikachu', 'base_experience': 112, 'image': 'url'}
    pokemon2 = {'name': 'Charmander', 'base_experience': 62, 'image': 'url'}
    trade = Trade()
    trade.right_side = [pokemon1, pokemon2]
    trade.left_side = [pokemon1, pokemon2]
    trade.result = trade.is_fair()

    return trade
