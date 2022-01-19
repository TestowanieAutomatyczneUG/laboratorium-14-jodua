from behave import *
from src.Database import Database, DatabaseError
from src.Author import Author
from src.Book import Book
from unittest.mock import MagicMock

use_step_matcher("re")


# GIVEN


@given('there is an book database')
def step_impl(context):
    context.db = Database()


@given('api_call method mock, returning (?P<return_value>.+)')
def step_impl(context, return_value):
    context.db.api_call = MagicMock(return_value=return_value)


@given('api_call method mock, raising database error')
def step_impl(context):
    context.db.api_call = MagicMock(side_effect=DatabaseError)


@given('there is an writer with first_name (?P<first_name>.+), second_name (?P<last_name>.+), email (?P<email>.+)')
def step_impl(context, first_name, last_name, email):
    context.writer = Author(first_name, last_name, email)


@given('there is a book (?P<title>.+) with ISBN (?P<isbn>.+)')
def step_impl(context, title, isbn):
    context.book = Book(title, context.writer, isbn)
# WHEN


@when('function (?P<function>.+) is called with argument (?P<arg>.+)')
def step_impl(context, function, arg):
    try:
        context.result = getattr(context.db, function)(arg)
    except Exception as x:
        context.error = x


@when('function (?P<function>.+) is called')
def step_impl(context, function):
    try:
        context.result = getattr(context.db, function)()
    except Exception as x:
        context.error = x


@when('we add new book to database')
def step_impl(context):
    try:
        context.result = context.db.add_book(context.book)
    except Exception as x:
        context.error = x


@when('we update book in database')
def step_impl(context):
    try:
        context.result = context.db.edit_book(context.book)
    except Exception as x:
        context.error = x

# THEN


@then('we get (?P<result>.+) as result')
def step_impl(context, result):
    assert context.result == result


@Then('DatabaseError is raised')
def step_impl(context):
    assert isinstance(context.error, DatabaseError)
