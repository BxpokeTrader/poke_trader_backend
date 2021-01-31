from behave import given

from test.util.test_utils import create_default_trade


@given('that 2 trades are already saved')
def step_impl(context):
    trade1 = create_default_trade()
    trade2 = create_default_trade()
    trade1.result = trade1.is_fair()
    trade2.result = trade2.is_fair()

    trade1.save()
    trade2.save()
