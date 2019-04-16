import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from Home10.additional_data import random_string, presence_num_of_elements


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    #driver = webdriver.Firefox(executable_path = r"/home/qa/Downloads/geckodriver")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(scope='module')
def log_in_log_out(driver):
    driver.get('http://127.0.0.1/oxwall')
    driver.find_element(By.CLASS_NAME, "ow_signin_label").click()
    sign_in_window = driver.find_element(By.CLASS_NAME, "floatbox_container")
    driver.find_element(By.NAME, "identity").send_keys((Keys.CONTROL, 'a'), Keys.DELETE)
    driver.find_element(By.NAME, "identity").send_keys('admin')
    driver.find_element(By.NAME, "password").send_keys((Keys.CONTROL, 'a'), Keys.DELETE)
    driver.find_element(By.NAME, "password").send_keys('admin')
    driver.find_element(By.NAME, "submit").click()

    wait = WebDriverWait(driver, 10)
    wait.until_not(expected_conditions.visibility_of(sign_in_window))

    yield
    profile = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div[5]/a')
    log_out_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div/div[5]/div/div/div[2]/ul/li[7]/div/a")

    action = ActionChains(driver)
    action.move_to_element(profile).move_to_element(log_out_button).click().perform()

    driver.quit()


@pytest.fixture()
def create_new_comment(driver):
    input_text = random_string(1, 300)
    all_comments = driver.find_elements(By.CLASS_NAME, 'ow_newsfeed_content')
    driver.find_element(By.NAME, "status").send_keys(input_text)
    driver.find_element(By.NAME, "save").click()
    expected_comments_value = len(all_comments) + 1
    wait = WebDriverWait(driver, 10)
    wait.until(presence_num_of_elements((By.CLASS_NAME, 'ow_newsfeed_content'), expected_comments_value))

    yield
    action = ActionChains(driver)
    driver.find_element(By.CLASS_NAME, "ow_newsfeed_content").click()
    more = driver.find_element(By.CLASS_NAME, "ow_context_more")
    delete = driver.find_element(By.CLASS_NAME, "newsfeed_remove_btn")
    action.move_to_element(more).move_to_element(delete).click().perform()
    driver.switch_to_alert().accept()
    sleep(1)