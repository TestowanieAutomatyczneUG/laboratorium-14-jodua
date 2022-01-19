from behave import *
from src.Book import Book
from src.Author import Author

use_step_matcher("re")

# EN


@given('there is an title (?P<title>.+)')
def step_impl(context, title):
    context.title = title


@given('there is an author (?P<first_name>.+), (?P<last_name>.+), (?P<email>.+)')
def step_impl(context, first_name, last_name, email):
    context.author = Author(first_name, last_name, email)


@given('there is an ISBN (?P<isbn>.+)')
def step_impl(context, isbn):
    context.isbn = isbn


@when('the book is created')
def step_imp(context):
    try:
        context.book = Book(
            context.title, context.author, context.isbn)
    except Exception as ex:
        context.error = ex


@then('book data is equal to (?P<data>.+)')
def step_imp(context, data):
    assert context.book.title+" "+context.book.ISBN == data

# ES


@given('hay un titulo (?P<title>.+)')
def step_impl(context, title):
    context.title = title


@given('Hay un autor (?P<first_name>.+), (?P<last_name>.+), (?P<email>.+)')
def step_impl(context, first_name, last_name, email):
    context.author = Author(first_name, last_name, email)


@given('hay un ISBN (?P<isbn>.+)')
def step_impl(context, isbn):
    context.isbn = isbn


@when('se crea el libro')
def step_imp(context):
    try:
        context.book = Book(
            context.title, context.author, context.isbn)
    except Exception as ex:
        context.error = ex


@then('los datos del libro son iguales a (?P<data>.+)')
def step_imp(context, data):
    assert context.book.title+" "+context.book.ISBN == data
