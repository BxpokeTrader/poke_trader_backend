from behave import given, when, then

from trade.models import Trade, Pokemon

global result
global trade


@given('that I have the same pokemon in both sides')
def step_impl(context):
    pokemon1 = Pokemon(name='Charmander', base_experience=100)
    pokemon2 = Pokemon(name='Charmander', base_experience=100)
    global trade
    trade = Trade(left_side=[pokemon1.__str__()], right_side=[pokemon2.__str__()])


@given('that I have a pokemon with high value in the right side and a simple pokemon in the left side')
def step_impl(context):
    global trade
    simple_pokemon = Pokemon(name='Numel', base_experience=61)
    good_pokemon = Pokemon(name='Charizard', base_experience=240)
    trade = Trade(left_side=[simple_pokemon.__str__()], right_side=[good_pokemon.__str__()])
    trade.save()


@when('I request to verify it')
def step_impl(context):
    global result
    global trade
    print(trade.is_fair())
    result = trade.is_fair()


@then('the system returns "{expected_result}"')
def step_impl(context, expected_result):
    global result
    assert result == expected_result
