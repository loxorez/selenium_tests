from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from Home11.custom_expected_conditions import presence_num_of_elements_gt, presence_num_of_elements_eq, random_string
from Home11.locators import DefaultPageLocators, SignInPageLocators, DashboardPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DefaultPage(object):
    """Default page methods placed here"""

    def __init__(self, driver):
        self.driver = driver

        self.sign_in_name = DefaultPageLocators.SIGN_IN
        self.sign_up_name = DefaultPageLocators.SIGN_UP

    def click_sign_in(self):
        # Click Sign In button
        self.driver.find_element(*self.sign_in_name).click()

    def click_sign_up(self):
        # Click Sign Up button
        self.driver.find_element(*self.sign_up_name).click()

    def log_out(self):
        # Open user profile, clicking log out button
        driver = self.driver
        profile_button = driver.find_element(*DashboardPageLocators.USER_PROFILE)
        log_out_button = driver.find_element(*DashboardPageLocators.SIGN_OUT)
        action = ActionChains(driver)
        action.move_to_element(profile_button).move_to_element(log_out_button).click().perform()
        driver.quit()


class SignInPage(object):
    """SignIn page methods placed here"""
    def __init__(self, driver):
        self.driver = driver

        self.login_window_class = SignInPageLocators.LOGIN_WINDOW
        self.username_name = SignInPageLocators.USER_NAME
        self.password_name = SignInPageLocators.PASSWORD
        self.submit_name = SignInPageLocators.SUBMIT
        self.remember_box = SignInPageLocators.REMEMBER_BOX

    def send_user_name(self, user):
        # Send user_name
        self.driver.find_element(*self.username_name).clear()
        self.driver.find_element(*self.username_name).send_keys(user)

    def send_password(self, password):
        # Send password
        self.driver.find_element(*self.password_name).clear()
        self.driver.find_element(*self.password_name).send_keys(password)

    def submit(self):
        self.driver.find_element(*self.submit_name).click()


class DashboardPage(object):
    """Dashboard page methods placed here"""
    def __init__(self, driver):
        self.driver = driver

        self.status_name = DashboardPageLocators.STATUS
        self.status_add_form_name = DashboardPageLocators.STATUS_ADD_FORM
        self.status_submit_name = DashboardPageLocators.STATUS_SUBMIT
        self.status_more_link_text = DashboardPageLocators.STATUS_MORE_BUTTON
        self.status_context_name = DashboardPageLocators.STATUS_CONTEXT
        self.status_delete_name = DashboardPageLocators.STATUS_DELETE
        self.user_profile_xpath = DashboardPageLocators.USER_PROFILE
        self.sign_out_xpath = DashboardPageLocators.SIGN_OUT
        self.inform_message_name = DashboardPageLocators.INFORM_MESSAGE
        self.inform_message_close_name = DashboardPageLocators.INFORM_MESSAGE_CLOSE
        self.like_number_name = DashboardPageLocators.LIKE_COUNTER
        self.like_status_name = DashboardPageLocators.LIKE_STATUS
        self.like_string_name = DashboardPageLocators.LIKE_STRIG
        self.status_counter_name = DashboardPageLocators.STATUS_COUNTER
        self.status_form_name = DashboardPageLocators.STATUS_FORM
        self.status_inside_comment_name = DashboardPageLocators.STATUS_INSIDE_COMMENT_FORM
        self.status_inside_button_name = DashboardPageLocators.STATUS_INSIDE_BUTTON
        self.status_added_time_name = DashboardPageLocators.STATUS_ADDED_TIME

    def random_string_gen(self, x, y):
        # Return special string in specified range
        return random_string(x , y)

    def all_statuses(self):
        # Find all comments
        return self.driver.find_elements(*self.status_name)

    def inform_message_box(self):
        # Find inform form
        return self.driver.find_element(*self.inform_message_name)

    def close_inform_message_box(self):
        # Close inform form
        self.driver.find_element(*self.inform_message_close_name).click()

    def create_new_status(self, input_text):
        # Find form to add comment, fill form
        self.driver.find_element(*self.status_add_form_name).send_keys(input_text)
        # Submit comment
        self.driver.find_element(*self.status_submit_name).click()

    def delete_status(self):
        # Delete last status
        driver = self.driver
        action = ActionChains(driver)
        driver.find_element(*self.status_name).click()
        action.move_to_element(driver.find_element(*self.status_context_name)).move_to_element(driver.find_element(*self.status_delete_name)).click().perform()
        driver.switch_to_alert().accept()

    def see_more_button_click(self):
        # Find see more button, perform it
        self.driver.find_element(*self.status_more_link_text).click()

    def status_add_click(self):
        # Select status text form
        self.driver.find_element(*self.status_add_form_name).click()

    def status_submit(self):
        # Click status submit button
        self.driver.find_element(*self.status_submit_name).click()

    def like_status(self):
        # Click like button
        self.driver.find_element(*self.like_status_name).click()

    def status_likes_value(self):
        # Return status like value
        return int(self.driver.find_element(*self.like_number_name).text)

    def status_comment_value(self):
        # Return status inside comment value
        return int(self.driver.find_element(*self.status_counter_name).text)

    def status_inside_opens(self):
        # Open inside status form
        self.driver.find_element(*self.status_inside_button_name).click()

    def status_adding_time(self):
        # Click status adding time button, open detail status in new windows
        self.driver.find_element(*self.status_added_time_name).send_keys(Keys.CONTROL, Keys.ENTER)

    def send_inside_comment(self):
        # Post inside comment in special status
        wait = WebDriverWait(self.driver, 10)
        current_comment_counter = int(self.driver.find_element(*self.status_counter_name).text)
        self.driver.find_element(*self.status_inside_comment_name).send_keys(random_string(1, 150), Keys.ENTER)
        wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "newsfeed_counter_comments"), str(current_comment_counter+1)))

    def wait_until_new_status_appears(self, old_comments_list):
        # Explicit wait till new status appears in newsfeed
        wait = WebDriverWait(self.driver, 10)
        new_statuses = wait.until(presence_num_of_elements_gt((By.CLASS_NAME, 'ow_newsfeed_content'), len(old_comments_list)))
        # Return all comments include new one
        return new_statuses

    def wait_until_status_deletes(self, old_comments_list):
        # Explicit wait till new status deletes from newsfeed
        wait = WebDriverWait(self.driver, 10)
        new_statuses = wait.until(presence_num_of_elements_eq((By.CLASS_NAME, 'ow_newsfeed_content'), len(old_comments_list)))
        # Return all comments include new one
        return new_statuses

    def wait_until_like_string_appears(self):
        # Explicit wait till like message appears
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of(self.driver.find_element(*self.like_string_name)))

    def wait_until_status_form_appears(self):
        # Explicit wait till comment form inside status appears
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of(self.driver.find_element(*self.status_form_name)))

