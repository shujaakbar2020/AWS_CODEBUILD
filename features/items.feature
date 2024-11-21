Feature: Manage Items
  As a user
  I want to manage items in the Flask API
  So that I can add, view, and delete items

  Scenario: Get all items
    Given the API is running
    When I send a GET request to "/items"
    Then the response status code should be 200

  Scenario: Add a new item
    Given the API is running
    When I send a POST request to "/items" with data {"item": "Book"}
    Then the response status code should be 201
    And the response should contain "message" as "Item added"
    And the response should contain the added "item" as "Book"
