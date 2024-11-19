Feature: User Login

  Scenario: Successful Login
    Given a registered user exists
    When the user logs in with correct credentials
    Then the user sees the dashboard
