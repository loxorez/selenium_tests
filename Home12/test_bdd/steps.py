import pytest
from pytest_bdd import given, when, then, scenario

from Home12.pages import DashboardPage, DefaultPage
from models.user import User


# Given Steps

@given("initial amount os statuses")
def initial_statuses(application, driver):
    dashboard = DashboardPage(driver)
    return dashboard.all_statuses_elements


@given("logged user")
@pytest.fixture(scope="session")
def logged_user(application, config, driver):
    user = User(**config["web"])
    default_page = DefaultPage(driver)
    sign_in_page = default_page.click_sign_in()
    sign_in_page.send_user_name(user.username)
    sign_in_page.send_password(user.password)
    sign_in_page.submit()
    yield user
    default_page.log_out()


@given("initial likes value")
def initial_status_likes(driver):
    dashboard = DashboardPage(driver)
    current_like_counter = dashboard.all_statuses_elements[0].likes_value
    return current_like_counter


@given("create new status")
def status_create(driver):
    dashboard = DashboardPage(driver)
    input_text = dashboard.random_string_gen(1, 300)
    all_existing_statuses = dashboard.all_statuses_elements
    dashboard.create_new_status(input_text)
    dashboard.wait_until_new_status_appears(all_existing_statuses)


@given("initial status inside comments value")
def initial_statuses_comments(application, driver):
    dashboard = DashboardPage(driver)
    return dashboard.all_statuses_elements[0].status_value


# When Steps

@when("I add status with <text>")
def create_status(text, driver):
    dashboard = DashboardPage(driver)
    dashboard.create_new_status(text)


@when("status input field is empty and contain <placeholder_text>")
def empty_status_placeholder(driver, placeholder_text):
    dashboard = DashboardPage(driver)
    assert dashboard.status_input_field.placeholder == placeholder_text


@when("i submit empty status")
def empty_status_submit(driver):
    dashboard = DashboardPage(driver)
    dashboard.status_add_click()
    dashboard.status_submit()


@when("user click like button")
def like_status_button_click(driver):
    dashboard = DashboardPage(driver)
    dashboard.like_status()
    dashboard.wait_until_like_string_appears()


@when("user add inside comments in status")
def add_inside_comments(driver):
    dashboard = DashboardPage(driver)
    comment_number = 5
    dashboard.status_inside_opens()
    dashboard.wait_until_status_form_appears()
    for i in range(comment_number):
        dashboard.send_inside_comment()


# Then steps

@then("a new status block appears")
def new_status_block_appear(initial_statuses, driver):
    dashboard = DashboardPage(driver)
    dashboard.wait_until_new_status_appears(initial_statuses)


@then("this status block has <text> and author")
def check_status_data(text, logged_user, driver):
    dashboard = DashboardPage(driver)
    new_status_in_newsfeed = dashboard.all_statuses_elements[0]
    assert new_status_in_newsfeed.text == text
    assert new_status_in_newsfeed.user.username == logged_user.username


@then("i click button to show whole status")
def see_more_click(driver):
    dashboard = DashboardPage(driver)
    dashboard.see_more_button_click()


@then("inform message box appears with <results_box_message>")
def inform_message_box(driver, results_box_message):
    dashboard = DashboardPage(driver)
    result_message = dashboard.inform_message_box.text
    dashboard.close_inform_message_box()
    assert result_message == results_box_message


@then("i delete created status, initial amount of statuses the same as after delete")
def amount_of_statuses_after_delete(driver, initial_statuses):
    dashboard = DashboardPage(driver)
    dashboard.delete_status()
    all_statuses_after_delete = dashboard.wait_until_status_deletes(initial_statuses)
    assert len(all_statuses_after_delete) == len(initial_statuses)


@then("likes values increased")
def amount_of_status_likes_after_like(driver, initial_status_likes):
    dashboard = DashboardPage(driver)
    new_like_counter = dashboard.all_statuses_elements[0].likes_value
    assert new_like_counter == initial_status_likes+1


@then("like string has user likes message")
def like_string_user(driver, logged_user):
    dashboard = DashboardPage(driver)
    assert dashboard.all_statuses_elements[0].like_string == logged_user.real_name + " likes this"


@then("inside status comments value has increased")
def inside_status_comments_value(driver, initial_statuses_comments):
    dashboard = DashboardPage(driver)
    new_comment_counter = dashboard.all_statuses_elements[0].status_value
    assert new_comment_counter == initial_statuses_comments + 5


