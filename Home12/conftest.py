import json
import os
import pytest
from selenium import webdriver
from Home12.pages import DefaultPage, DashboardPage
from models.user import User
from time import sleep


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def application(driver):
    return driver.get("http://127.0.0.1/oxwall/")


@pytest.fixture(scope='session')
def user_log_in_log_out(driver, application):
    user = User(username='admin', password='admin', real_name='Admin')
    default_page = DefaultPage(driver)
    sign_in_page = default_page.click_sign_in()
    sign_in_page.send_user_name(user.username)
    sign_in_page.send_password(user.password)
    sign_in_page.submit()
    yield user
    default_page.log_out()


@pytest.fixture()
def create_new_comment(driver):
    dashboard = DashboardPage(driver)
    input_text = dashboard.random_string_gen(1, 300)
    all_existing_statuses = dashboard.all_statuses_elements
    dashboard.create_new_status(input_text)
    dashboard.wait_until_new_status_appears(all_existing_statuses)
    yield
    dashboard.delete_status()
    sleep(1)


# Open values to parametrize status tests
json_status_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), "json_data", "status_data.json")
with open(json_status_data, 'r') as file:
    json_data = file.read()
    statuses_list = json.loads(json_data)

# Status text, using parametrize
@pytest.fixture(params=statuses_list, ids=[str(status) for status in statuses_list])
def status_text_parametrize(request):
    return request.param
