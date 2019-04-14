from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from Home10.additional_data import random_string, presence_num_of_elements


def test_create_short_post(driver, log_in_log_out):
    input_text = random_string(1, 300)
    all_comments = driver.find_elements(By.CLASS_NAME, 'ow_newsfeed_content')
    driver.find_element(By.NAME, "status").send_keys(input_text)
    driver.find_element(By.NAME, "save").click()
    expected_comments_value = len(all_comments) + 1

    wait = WebDriverWait(driver, 10)
    new_comments = wait.until(presence_num_of_elements((By.CLASS_NAME, 'ow_newsfeed_content'), expected_comments_value))
    assert new_comments[0].text == input_text
#

def test_create_long_post(driver, log_in_log_out):
    input_text = random_string(500, 800)
    all_comments = driver.find_elements(By.CLASS_NAME, 'ow_newsfeed_content')
    driver.find_element(By.NAME, "status").send_keys(input_text)
    driver.find_element(By.NAME, "save").click()
    expected_comments_value = len(all_comments) + 1

    wait = WebDriverWait(driver, 10)
    wait.until(presence_num_of_elements((By.CLASS_NAME, 'ow_newsfeed_content'), expected_comments_value))
    driver.find_element(By.LINK_TEXT, 'See more').click()
    new_comments = driver.find_elements(By.CLASS_NAME, 'ow_newsfeed_content')
    assert new_comments[0].text == input_text


def test_delete_post(driver, log_in_log_out):
    input_text = random_string(1, 300)
    all_comments = driver.find_elements(By.CLASS_NAME, 'ow_newsfeed_content')
    driver.find_element(By.NAME, "status").send_keys(input_text)
    driver.find_element(By.NAME, "save").click()
    expected_comments_value = len(all_comments) + 1

    wait = WebDriverWait(driver, 10)
    wait.until(presence_num_of_elements((By.CLASS_NAME, 'ow_newsfeed_content'), expected_comments_value))

    action = ActionChains(driver)
    driver.find_element(By.CLASS_NAME, "ow_newsfeed_content").click()
    more = driver.find_element(By.CLASS_NAME, "ow_context_more")
    delete = driver.find_element(By.CLASS_NAME, "newsfeed_remove_btn")
    action.move_to_element(more).move_to_element(delete).click().perform()
    driver.switch_to_alert().accept()

    all_comments_after_delete = wait.until(presence_num_of_elements((By.CLASS_NAME, 'ow_newsfeed_content'),
                                                                    len(all_comments)))
    assert len(all_comments) == len(all_comments_after_delete)


def test_like_counter(driver, log_in_log_out, create_new_comment):
    current_like_counter = driver.find_element(By.CLASS_NAME, "newsfeed_counter_likes").text
    driver.find_element(By.CLASS_NAME, "ow_miniic_like").click()
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.visibility_of(driver.find_element(By.CLASS_NAME, "newsfeed_likes_string")))
    new_like_counter = driver.find_element(By.CLASS_NAME, "newsfeed_counter_likes").text
    assert int(new_like_counter) == int(current_like_counter)+1


def test_time_till_post_added_link(driver, log_in_log_out, create_new_comment):
    driver.find_element(By.CLASS_NAME, "ow_newsfeed_date").send_keys(Keys.CONTROL, Keys.ENTER)
    window_handles = driver.window_handles
    driver.switch_to_window(window_handles[1])
    driver.close()
    driver.switch_to_window(window_handles[0])
    assert len(window_handles) == 2


def test_add_inner_comment(driver, log_in_log_out, create_new_comment):
    input_inner_text = random_string(1, 150)
    driver.find_element(By.CLASS_NAME, "ow_miniic_comment").click()
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.visibility_of(driver.find_element(By.CLASS_NAME, "ow_comments_form_wrap")))
    driver.find_element(By.CLASS_NAME, "comments_fake_autoclick").send_keys(input_inner_text, Keys.ENTER)
    comment = wait.until(expected_conditions.visibility_of(driver.find_element(By.CLASS_NAME, "ow_comments_content")))
    assert comment.text == input_inner_text
