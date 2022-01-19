from behave import *
from src.ISBNValidator import ISBNValidator

use_step_matcher("re")


# GIVEN

@given('there is an ISBNValidator')
def step_impl(context):
    context.isbn_calculator = ISBNValidator()
# WHEN


@when('we pass (?P<string>.+) to validate method')
def step_impl(context, string):
    context.result = context.isbn_calculator.validate(string)

# THEN


@then("we get (?P<result>.+) as result")
def step_impl(context, result):
    if result == "false":
        assert context.result == False
    elif result == "true":
        assert context.result == True
    else:
        assert context.result == result
