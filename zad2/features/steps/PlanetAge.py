from behave import *
from src.PlanetAge import PlanetAge

use_step_matcher("re")


# GIVEN

@given('there is an PlanetAge')
def step_impl(context):
    context.planet_age = PlanetAge()
# WHEN


@when('we pass number (?P<number>[0-9]+) and planet (?P<planet>.+) to calculate method')
def step_impl(context, number, planet):
    context.result = context.planet_age.calculate(float(number), planet)


@when('we pass not a number as first argument')
def step_impl(context):
    try:
        context.result = context.planet_age.calculate("test", "Merkury")
    except Exception as ex:
        context.ex = ex


@when('we pass invalid planet type as second argument')
def step_impl(context):
    try:
        context.result = context.planet_age.calculate(123, 123)
    except Exception as ex:
        context.ex = ex


@when('we pass negative number to calculate method')
def step_impl(context):
    try:
        context.result = context.planet_age.calculate(-123, "Ziemia")
    except Exception as ex:
        context.ex = ex


@when('we pass invalid planet to calculate method')
def step_impl(context):
    try:
        context.result = context.planet_age.calculate(123123123, "Marek")
    except Exception as ex:
        context.ex = ex

# THEN


@then("we get (?P<number>.+) as result")
def step_impl(context, number):
    assert abs(context.result-float(number)) < 0.00001


@then("TypeError is raised")
def step_impl(context):
    assert isinstance(context.ex, TypeError)


@then("ValueError is raised")
def step_impl(context):
    assert isinstance(context.ex, ValueError)
