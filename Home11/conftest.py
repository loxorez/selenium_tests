import pytest
from selenium import webdriver
from Home11.pages import DefaultPage, SignInPage
from models.user import User
from Home11.pages import DashboardPage
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
    sign_in_page = SignInPage(driver)
    default_page.click_sign_in()
    sign_in_page.send_user_name(user.username)
    sign_in_page.send_password(user.password)
    sign_in_page.submit()
    yield
    default_page.log_out()


@pytest.fixture()
def create_new_comment(driver):
    dashboard = DashboardPage(driver)
    input_text = dashboard.random_string_gen(1, 300)
    all_existing_statuses = dashboard.all_statuses()
    dashboard.create_new_status(input_text)
    dashboard.wait_until_new_status_appears(all_existing_statuses)

    yield
    dashboard.delete_status()
    sleep(1)


