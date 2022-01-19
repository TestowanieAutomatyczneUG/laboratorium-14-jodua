from behave import *
from src.Author import Author

use_step_matcher("re")

# EN


@given('there is an first_name (?P<first_name>.+)')
def step_impl(context, first_name):
    context.first_name = first_name


@given('there is an last_name (?P<last_name>.+)')
def step_impl(context, last_name):
    context.last_name = last_name


@given('there is an email (?P<email>.+)')
def step_impl(context, email):
    context.email = email


@given('there is an invalid email')
def step_impl(context):
    context.email = 123


@when('the author is created')
def step_imp(context):
    try:
        context.author = Author(
            context.first_name, context.last_name, context.email)
    except Exception as ex:
        context.error = ex


@then('author first_name is equal to (?P<first_name>.+)')
def step_imp(context, first_name):
    assert context.author.first_name == first_name


@then('author full name is equal to (?P<full_name>.+)')
def step_imp(context, full_name):
    assert context.author.first_name+" "+context.author.last_name == full_name


@then('author last_name is equal to (?P<last_name>.+)')
def step_imp(context, last_name):
    assert context.author.last_name == last_name


@then('author email is equal to (?P<email>.+)')
def step_imp(context, email):
    assert context.author.email == email


@then('TypeError is raised')
def step_imp(context):
    assert isinstance(context.error, TypeError)


# ES
@given('hay un nombre (?P<first_name>.+)')
def step_impl(context, first_name):
    context.first_name = first_name


@given('hay un apellido (?P<last_name>.+)')
def step_impl(context, last_name):
    context.last_name = last_name


@given('hay un correo (?P<email>.+)')
def step_impl(context, email):
    context.email = email


@given('!hay un correo inválido')
def step_impl(context):
    context.email = 123


@when('Se crea el autor')
def step_imp(context):
    try:
        context.author = Author(
            context.first_name, context.last_name, context.email)
    except Exception as ex:
        context.error = ex


@then('el nombre completo del autor es igual a (?P<full_name>.+)')
def step_imp(context, full_name):
    assert context.author.first_name+" "+context.author.last_name == full_name


@then('el nombre del autor es igual a (?P<first_name>.+)')
def step_imp(context, first_name):
    assert context.author.first_name == first_name


@then('el apellido del autor es igual a (?P<last_name>.+)')
def step_imp(context, last_name):
    assert context.author.last_name == last_name


@then('el correo electrónico del autor es igual a (?P<email>.+)')
def step_imp(context, email):
    assert context.author.email == email


@then('Se genera TypeError')
def step_imp(context):
    assert isinstance(context.error, TypeError)
