from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from Home10.additional_data import random_string, presence_num_of_elements
import random


def test_create_short_post(driver, log_in_log_out):
    input_text = random_string(1, 300)
    all_comments = driver.find_elements(By.CLASS_NAME, 'ow_newsfeed_content')
    driver.find_element(By.NAME, "status").send_keys(input_text)
    driver.find_element(By.NAME, "save").click()
    expected_comments_value = len(all_comments) + 1

    wait = WebDriverWait(driver, 10)
    new_comments = wait.until(presence_num_of_elements((By.CLASS_NAME, 'ow_newsfeed_content'), expected_comments_value))
    assert new_comments[0].text == input_text


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


def test_empty_form(driver, log_in_log_out):
     driver.find_element(By.NAME, "status").click()
     driver.find_element(By.NAME, "save").click()
     result_message = driver.find_element(By.CLASS_NAME, "ow_message_node").text
     assert result_message == "PLEASE FILL THE FORM PROPERLY"


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


def test_comment_counter(driver, log_in_log_out, create_new_comment):
    comment_number = random.randint(1, 5)
    current_comment_counter = driver.find_element(By.CLASS_NAME, "newsfeed_counter_comments").text
    driver.find_element(By.CLASS_NAME, "ow_miniic_comment").click()
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.visibility_of(driver.find_element(By.CLASS_NAME, "ow_comments_form_wrap")))
    for i in range(comment_number):
        driver.find_element(By.CLASS_NAME, "comments_fake_autoclick").send_keys(random_string(1, 150), Keys.ENTER)
    wait.until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "newsfeed_counter_comments"), str(comment_number)))
    new_comment_counter = driver.find_element(By.CLASS_NAME, "newsfeed_counter_comments").text
    assert int(new_comment_counter) == int(current_comment_counter)+comment_number


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


def test_change_avatar(driver, log_in_log_out):
    driver.refresh()
    driver.find_element(By.LINK_TEXT, "Change avatar").click()
    wait = WebDriverWait(driver, 10)
    all_avatars = driver.find_elements(By.CLASS_NAME, "ow_photo_avatar_hover")
    all_avatars[0].click()
    wait.until(expected_conditions.visibility_of(driver.find_element(By.CLASS_NAME, "jcrop-tracker")))
    driver.find_element(By.ID, "avatar-crop-btn").click()
    wait.until_not(expected_conditions.visibility_of(driver.find_element(By.CLASS_NAME, "floatbox_container")))
    result_message = driver.find_element(By.CLASS_NAME, "ow_message_node").text
    assert result_message == "AVATAR HAS BEEN CHANGED"


def test_view_more_feed(driver, log_in_log_out):
    driver.refresh()
    all_news = driver.find_elements(By.CLASS_NAME, "ow_newsfeed_body")
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.CLASS_NAME, "ow_newsfeed_view_more").click()
    more_news = wait.until(presence_num_of_elements((By.CLASS_NAME, "ow_newsfeed_body"), 20))
    assert len(more_news) > len(all_news)

