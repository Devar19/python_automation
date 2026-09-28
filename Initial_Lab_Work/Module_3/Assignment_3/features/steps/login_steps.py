from behave import given, when, then
from features.pages.login_page import LoginPage


@given("I am on the SauceDemo login page")
def open_login_page(context):

    context.driver.get(
        "https://www.saucedemo.com/"
    )


@when(
    'I login using username "{username}" '
    'and password "{password}"'
)
def login_with_credentials(context, username, password):

    login_page = LoginPage(
        context.driver
    )

    login_page.login(
        username,
        password
    )


@then('the login result should be "{result}"')
def verify_login_result(context, result):

    if result == "success":

        assert "/inventory.html" in (context.driver.current_url)

    elif result == "error":

        login_page = LoginPage(
            context.driver
        )

        error_message = (
            login_page.get_error_message()
        )

        assert error_message

    else:

        raise ValueError(
            f"Unknown login result: {result}"
        )