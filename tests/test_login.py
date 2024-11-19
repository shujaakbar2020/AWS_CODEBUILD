from pytest_bdd import scenarios, given, when, then

scenarios("features/login.feature")

@given("a registered user exists")
def registered_user():
    # Setup user logic here
    pass

@when("the user logs in with correct credentials")
def user_logs_in():
    # Login logic here
    pass

@then("the user sees the dashboard")
def sees_dashboard():
    # Assert dashboard view here
    pass
