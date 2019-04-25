from Home11.pages import DashboardPage


def test_create_short_status(driver, user_log_in_log_out):
    # Create short status, verify it presence
    dashboard = DashboardPage(driver)
    input_text = dashboard.random_string_gen(1, 300)
    all_existing_statuses = dashboard.all_statuses()
    dashboard.create_new_status(input_text)
    new_statuses_in_newsfeed = dashboard.wait_until_new_status_appears(all_existing_statuses)
    assert new_statuses_in_newsfeed[0].text == input_text


def test_create_long_status(driver, user_log_in_log_out):
    # Create long status, verify it presence
    dashboard = DashboardPage(driver)
    input_text = dashboard.random_string_gen(500, 800)
    all_existing_statuses = dashboard.all_statuses()
    dashboard.create_new_status(input_text)
    dashboard.wait_until_new_status_appears(all_existing_statuses)
    dashboard.see_more_button_click()
    new_comments_in_newsfeed = dashboard.wait_until_new_status_appears(all_existing_statuses)
    assert new_comments_in_newsfeed[0].text == input_text


def test_empty_status(driver, user_log_in_log_out):
    # Try to create empty status
    dashboard = DashboardPage(driver)
    dashboard.status_add_click()
    dashboard.status_submit()
    result_message = dashboard.inform_message_box().text
    dashboard.close_inform_message_box()
    assert result_message == "PLEASE FILL THE FORM PROPERLY"


def test_delete_status(driver, user_log_in_log_out):
    # Create status, instantly delete it
    dashboard = DashboardPage(driver)
    input_text = dashboard.random_string_gen(1, 300)
    all_existing_statuses = dashboard.all_statuses()
    dashboard.create_new_status(input_text)
    dashboard.wait_until_new_status_appears(all_existing_statuses)
    dashboard.delete_status()
    all_comments_after_delete = dashboard.wait_until_status_deletes(all_existing_statuses)
    assert len(all_comments_after_delete) == len(all_existing_statuses)


def test_like_counter(driver, user_log_in_log_out, create_new_comment):
    # Test likes counter
    dashboard = DashboardPage(driver)
    current_like_counter = dashboard.status_likes_value()
    dashboard.like_status()
    dashboard.wait_until_like_string_appears()
    new_like_counter = dashboard.status_likes_value()
    assert new_like_counter == current_like_counter+1


def test_inside_status_counter(driver, user_log_in_log_out, create_new_comment):
    # test comment counter
    dashboard = DashboardPage(driver)
    comment_number = 5
    current_comment_counter = dashboard.status_comment_value()
    dashboard.status_inside_opens()
    dashboard.wait_until_status_form_appears()
    for i in range(comment_number):
        dashboard.send_inside_comment()
    new_comment_counter = dashboard.status_comment_value()
    assert int(new_comment_counter) == int(current_comment_counter)+comment_number


def test_time_till_post_added_link(driver, user_log_in_log_out, create_new_comment):
    # Test link that shows passed time after status adding
    dashboard = DashboardPage(driver)
    dashboard.status_adding_time()
    window_handles = driver.window_handles
    driver.switch_to_window(window_handles[1])
    driver.close()
    driver.switch_to_window(window_handles[0])
    assert len(window_handles) == 2


# TODO: implement fallowing tests using Page Object pattern
# def test_add_inner_comment(driver, log_in_log_out, create_new_comment):
#     input_inner_text = random_string(1, 150)
#     current_inner_comment_counter = driver.find_elements(By.CLASS_NAME, "ow_comments_content")
#     driver.find_element(By.CLASS_NAME, "ow_miniic_comment").click()
#     wait = WebDriverWait(driver, 10)
#     wait.until(expected_conditions.visibility_of(driver.find_element(By.CLASS_NAME, "ow_comments_form_wrap")))
#     driver.find_element(By.CLASS_NAME, "comments_fake_autoclick").send_keys(input_inner_text, Keys.ENTER)
#     comments = wait.until(presence_num_of_elements_gt((By.CLASS_NAME, "ow_comments_content"), len(current_inner_comment_counter)))
#     assert comments[0].text == input_inner_text
#
#
# def test_change_avatar(driver, log_in_log_out):
#     driver.refresh()
#     driver.find_element(By.LINK_TEXT, "Change avatar").click()
#     wait = WebDriverWait(driver, 10)
#     all_avatars = driver.find_elements(By.CLASS_NAME, "ow_photo_avatar_hover")
#     all_avatars[0].click()
#     wait.until(expected_conditions.visibility_of(driver.find_element(By.CLASS_NAME, "jcrop-tracker")))
#     driver.find_element(By.ID, "avatar-crop-btn").click()
#     wait.until_not(expected_conditions.visibility_of(driver.find_element(By.CLASS_NAME, "floatbox_container")))
#     result_message = driver.find_element(By.CLASS_NAME, "ow_message_node").text
#     assert result_message == "AVATAR HAS BEEN CHANGED"
#
#
# def test_view_more_feed(driver, log_in_log_out):
#     driver.refresh()
#     all_news = driver.find_elements(By.CLASS_NAME, "ow_newsfeed_body")
#     wait = WebDriverWait(driver, 10)
#     driver.find_element(By.CLASS_NAME, "ow_newsfeed_view_more").click()
#     more_news = wait.until(presence_num_of_elements_gt((By.CLASS_NAME, "ow_newsfeed_body"), len(all_news)))
#     assert len(more_news) > len(all_news)


