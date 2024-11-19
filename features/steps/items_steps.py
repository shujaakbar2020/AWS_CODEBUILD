import requests
from behave import given, when, then

API_URL = "http://127.0.0.1:5000"

@given('the API is running')
def step_impl(context):
    response = requests.get(f"{API_URL}/")
    assert response.status_code == 200

@when('I send a GET request to "/items"')
def step_impl(context):
    context.response = requests.get(f"{API_URL}/items")

@when('I send a POST request to "/items" with data {data}')
def step_impl(context, data):
    context.response = requests.post(f"{API_URL}/items", json=eval(data))

@when('I send a DELETE request to "/items/{item_id}"')
def step_impl(context, item_id):
    context.response = requests.delete(f"{API_URL}/items/{item_id}")

@then('the response status code should be {status_code}')
def step_impl(context, status_code):
    assert context.response.status_code == int(status_code)

@then('the response should contain an empty "items" list')
def step_impl(context):
    assert context.response.json()["items"] == []

@then('the response should contain "message" as "{message}"')
def step_impl(context, message):
    assert context.response.json()["message"] == message

@then('the response should contain the added "item" as "{item}"')
def step_impl(context, item):
    assert context.response.json()["item"] == item

@then('the response should contain the removed "item" as "{item}"')
def step_impl(context, item):
    assert context.response.json()["item"] == item
