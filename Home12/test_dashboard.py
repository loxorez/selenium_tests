from Home12.pages import DashboardPage


def test_create_short_status(driver, user_log_in_log_out, status_text_parametrize):
    # Create short status, verify it presence
    dashboard = DashboardPage(driver)
    input_text = status_text_parametrize
    all_existing_statuses = dashboard.all_statuses_elements
    dashboard.create_new_status(input_text)
    dashboard.wait_until_new_status_appears(all_existing_statuses)
    new_status_in_newsfeed = dashboard.all_statuses_elements[0]
    assert new_status_in_newsfeed.text == input_text
    assert new_status_in_newsfeed.user.username == user_log_in_log_out.username


def test_create_long_status(driver, user_log_in_log_out):
    # Create long status, verify it presence
    dashboard = DashboardPage(driver)
    input_text = dashboard.random_string_gen(500, 800)
    all_existing_statuses = dashboard.all_statuses_elements
    dashboard.create_new_status(input_text)
    dashboard.wait_until_new_status_appears(all_existing_statuses)
    dashboard.see_more_button_click()
    new_status_in_newsfeed = dashboard.all_statuses_elements[0]
    assert new_status_in_newsfeed.text == input_text
    assert new_status_in_newsfeed.user.username == user_log_in_log_out.username


def test_empty_status(driver, user_log_in_log_out):
    # Try to create empty status
    dashboard = DashboardPage(driver)
    assert dashboard.status_input_field.placeholder == "What’s happening?"
    dashboard.status_add_click()
    dashboard.status_submit()
    result_message = dashboard.inform_message_box.text
    dashboard.close_inform_message_box()
    assert result_message == "PLEASE FILL THE FORM PROPERLY"


def test_delete_status(driver, user_log_in_log_out):
    # Create status, instantly delete it
    dashboard = DashboardPage(driver)
    input_text = dashboard.random_string_gen(1, 300)
    all_existing_statuses = dashboard.all_statuses_elements
    dashboard.create_new_status(input_text)
    dashboard.wait_until_new_status_appears(all_existing_statuses)
    dashboard.delete_status()
    all_statuses_after_delete = dashboard.wait_until_status_deletes(all_existing_statuses)
    assert len(all_statuses_after_delete) == len(all_existing_statuses)


def test_like_counter(driver, user_log_in_log_out, create_new_comment):
    # Test likes counter
    dashboard = DashboardPage(driver)
    current_like_counter = dashboard.all_statuses_elements[0].likes_value
    dashboard.like_status()
    dashboard.wait_until_like_string_appears()
    new_like_counter = dashboard.all_statuses_elements[0].likes_value
    assert new_like_counter == current_like_counter+1
    assert dashboard.all_statuses_elements[0].like_string == user_log_in_log_out.real_name + " likes this"


def test_inside_status_counter(driver, user_log_in_log_out, create_new_comment):
    # Test comment counter
    dashboard = DashboardPage(driver)
    comment_number = 5
    current_comment_counter = dashboard.all_statuses_elements[0].status_value
    dashboard.status_inside_opens()
    dashboard.wait_until_status_form_appears()
    for i in range(comment_number):
        dashboard.send_inside_comment()
    new_comment_counter = dashboard.all_statuses_elements[0].status_value
    assert new_comment_counter == current_comment_counter+comment_number


def test_time_till_post_added_link(driver, user_log_in_log_out, create_new_comment):
    # Test link that shows passed time after status adding
    dashboard = DashboardPage(driver)
    dashboard.status_adding_time()
    window_handles = driver.window_handles
    driver.switch_to_window(window_handles[1])
    driver.close()
    driver.switch_to_window(window_handles[0])
    assert len(window_handles) == 2


def test_add_inner_comment(driver, user_log_in_log_out, create_new_comment):
    # Test add inners status in special status, verify it presence
    dashboard = DashboardPage(driver)
    current_comment_counter = dashboard.all_statuses_elements[0].status_value
    dashboard.status_inside_opens()
    input_text = dashboard.send_inside_comment()
    assert input_text in dashboard.all_statuses_elements[0].inner_statuses[0].text
    assert user_log_in_log_out.real_name in dashboard.all_statuses_elements[0].inner_statuses[0].text
    assert dashboard.all_statuses_elements[0].status_value == current_comment_counter + 1


def test_change_avatar(driver, user_log_in_log_out):
    # Test avatar changing
    dashboard = DashboardPage(driver)
    avatar = dashboard.change_avatar()
    avatar.all_avatars[0].click()
    avatar.wait_until_crop_form_appears()
    avatar.apply_crop_click()
    avatar.wait_until_popup_becomes_invisible()
    assert avatar.inform_message_box.text == "AVATAR HAS BEEN CHANGED"
    avatar.close_inform_message_box()


def test_view_more_feed(driver, user_log_in_log_out):
    # Test view more news in newsfeed
    dashboard = DashboardPage(driver)
    all_news = dashboard.all_statuses_elements
    dashboard.view_more()
    dashboard.wait_until_new_status_appears(all_news)
    more_news = dashboard.all_statuses_elements
    assert len(more_news) > len(all_news)


# TODO: implement more tests using Page Object pattern

