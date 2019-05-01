from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Home12.custom_expected_conditions import presence_num_of_elements_gt, presence_num_of_elements_eq, random_string
from Home12.elements import StatusNewsfeedBody, InputTextElement


class BasePage(object):
    """Base page methods placed here"""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator),
                               message=f"Can't find element by locator {locator}")

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator),
                               message=f"Can't find elements by locator {locator}")

    def find_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator),
                               message=f"Can't find visible element by locator {locator}")


class DefaultPage(BasePage):
    """Default page elements locators and methods placed here"""
    SIGN_IN = (By.CLASS_NAME, "ow_signin_label")
    SIGN_UP = (By.CLASS_NAME, "ow_console_item_link")
    USER_PROFILE = (By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div[5]/a')
    SIGN_OUT = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div/div[5]/div/div/div[2]/ul/li[7]/div/a")
    INFORM_MESSAGE = (By.CLASS_NAME, "ow_message_node")
    INFORM_MESSAGE_CLOSE = (By.CLASS_NAME, 'close_button')
    POPUP_WINDOW = (By.CLASS_NAME, "floatbox_container")

    @property
    def inform_message_box(self):
        # Find inform form
        return self.driver.find_element(*self.INFORM_MESSAGE)

    def close_inform_message_box(self):
        # Close inform form
        self.driver.find_element(*self.INFORM_MESSAGE_CLOSE).click()

    def click_sign_in(self):
        # Click Sign In button
        self.driver.find_element(*self.SIGN_IN).click()
        return SignInPage(self.driver)

    def click_sign_up(self):
        # Click Sign Up button
        self.driver.find_element(*self.SIGN_UP).click()

    def log_out(self):
        # Open user profile, clicking log out button
        driver = self.driver
        profile_button = driver.find_element(*self.USER_PROFILE)
        log_out_button = driver.find_element(*self.SIGN_OUT)
        action = ActionChains(driver)
        action.move_to_element(profile_button).move_to_element(log_out_button).click().perform()
        driver.quit()

    def wait_until_popup_becomes_invisible(self):
        # Explicit wait till popup window disappear
        self.wait.until_not(EC.visibility_of(self.driver.find_element(*self.POPUP_WINDOW)))


class SignInPage(DefaultPage):
    """SignIn page elements locators and methods placed here"""
    LOGIN_WINDOW = (By.CLASS_NAME, "floatbox_container")
    USER_NAME = (By.NAME, "identity")
    PASSWORD = (By.NAME, "password")
    SUBMIT = (By.NAME, "submit")
    REMEMBER_BOX = (By.NAME, "remember")

    def send_user_name(self, user):
        # Send user_name
        self.driver.find_element(*self.USER_NAME).clear()
        self.driver.find_element(*self.USER_NAME).send_keys(user)

    def send_password(self, password):
        # Send password
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def submit(self):
        # Submit click
        self.driver.find_element(*self.SUBMIT).click()


class DashboardPage(DefaultPage):
    """Dashboard page elements locators and methods placed here"""
    STATUS_BODY = (By.CLASS_NAME, "ow_newsfeed_body")
    STATUS = (By.CLASS_NAME, 'ow_newsfeed_content')
    STATUS_ADD_FORM = (By.NAME, "status")
    STATUS_SUBMIT = (By.NAME, "save")
    STATUS_MORE_BUTTON = (By.LINK_TEXT, 'See more')
    STATUS_CONTEXT = (By.CLASS_NAME, "ow_context_more")
    STATUS_DELETE = (By.CLASS_NAME, "newsfeed_remove_btn")
    LIKE_STATUS = (By.CLASS_NAME, "ow_miniic_like")
    LIKE_STRING = (By.CLASS_NAME, "newsfeed_likes_string")
    STATUS_COUNTER = (By.CLASS_NAME, "newsfeed_counter_comments")
    STATUS_FORM = (By.CLASS_NAME, "ow_comments_form_wrap")
    STATUS_INSIDE_BUTTON = (By.CLASS_NAME, "ow_miniic_comment")
    STATUS_INSIDE_COMMENT_FORM = (By.CLASS_NAME, "comments_fake_autoclick")
    STATUS_ADDED_TIME = (By.CLASS_NAME, "ow_newsfeed_date")
    CHANGE_AVATAR = (By.LINK_TEXT, "Change avatar")
    VIEW_MORE = (By.CLASS_NAME, "ow_newsfeed_view_more")

    @property
    def all_statuses_elements(self):
        # Status field body, that contains all its elements
        return [StatusNewsfeedBody(item) for item in self.find_elements(self.STATUS_BODY)]

    @property
    def status_input_field(self):
        # Status input field, that contains all its elements
        return InputTextElement(self.find_visible_element(self.STATUS_ADD_FORM))

    @property
    def change_avatar(self):
        # Click change avatar button, open avatar selection window
        self.driver.find_element(*self.CHANGE_AVATAR).click()
        return ChangeAvatar(self.driver)

    def random_string_gen(self, x, y):
        # Return special string in specified range
        return random_string(x, y)

    def create_new_status(self, input_text):
        # Find form to add comment, fill form
        self.driver.find_element(*self.STATUS_ADD_FORM).send_keys(input_text)
        # Submit comment
        self.driver.find_element(*self.STATUS_SUBMIT).click()

    def delete_status(self):
        # Delete last status
        driver = self.driver
        action = ActionChains(driver)
        driver.find_element(*self.STATUS).click()
        action.move_to_element(driver.find_element(*self.STATUS_CONTEXT)).move_to_element(driver.find_element(*self.STATUS_DELETE)).click().perform()
        driver.switch_to_alert().accept()

    def see_more_button_click(self):
        # Find see more button, perform it
        self.driver.find_element(*self.STATUS_MORE_BUTTON).click()

    def status_add_click(self):
        # Select status text form
        self.driver.find_element(*self.STATUS_ADD_FORM).click()

    def status_submit(self):
        # Click status submit button
        self.driver.find_element(*self.STATUS_SUBMIT).click()

    def like_status(self):
        # Click like button
        self.driver.find_element(*self.LIKE_STATUS).click()

    def view_more(self):
        # Click view more button
        self.driver.find_element(*self.VIEW_MORE).click()

    def status_inside_opens(self):
        # Open inside status form
        self.driver.find_element(*self.STATUS_INSIDE_BUTTON).click()

    def status_adding_time(self):
        # Click status adding time button, open detail status in new windows
        self.driver.find_element(*self.STATUS_ADDED_TIME).send_keys(Keys.CONTROL, Keys.ENTER)

    def send_inside_comment(self):
        # Post inside comment in special status, return comment string
        input_text = random_string(1, 150)
        wait = WebDriverWait(self.driver, 10)
        current_comment_counter = int(self.driver.find_element(*self.STATUS_COUNTER).text)
        self.driver.find_element(*self.STATUS_INSIDE_COMMENT_FORM).send_keys(input_text, Keys.ENTER)
        wait.until(EC.text_to_be_present_in_element(self.STATUS_COUNTER, str(current_comment_counter+1)))
        return input_text

    def wait_until_new_status_appears(self, old_comments_list):
        # Explicit wait till new status appears in newsfeed
        wait = WebDriverWait(self.driver, 10)
        new_statuses = wait.until(presence_num_of_elements_gt(self.STATUS_BODY, len(old_comments_list)))
        # Return all comments include new one
        return new_statuses

    def wait_until_status_deletes(self, old_comments_list):
        # Explicit wait till new status deletes from newsfeed
        wait = WebDriverWait(self.driver, 10)
        new_statuses = wait.until(presence_num_of_elements_eq(self.STATUS_BODY, len(old_comments_list)))
        # Return all comments include new one
        return new_statuses

    def wait_until_like_string_appears(self):
        # Explicit wait till like message appears
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of(self.driver.find_element(*self.LIKE_STRING)))

    def wait_until_status_form_appears(self):
        # Explicit wait till comment form inside status appears
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of(self.driver.find_element(*self.STATUS_FORM)))


class ChangeAvatar(DefaultPage):
    """Change Avatar page elements locators and methods placed here"""
    AVATAR = (By.CLASS_NAME, "ow_photo_avatar_hover")
    CROP_AVATAR_FORM = (By.CLASS_NAME, "jcrop-tracker")
    CROP_AVATAR_BUTTON = (By.ID, "avatar-crop-btn")

    @property
    def all_avatars(self):
        # Return all existing avatars
        return self.driver.find_elements(*self.AVATAR)

    def apply_crop_click(self):
        # Apply avatar crop
        self.driver.find_element(*self.CROP_AVATAR_BUTTON).click()

    def wait_until_crop_form_appears(self):
        # Explicit wait till crop loaded
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of(self.driver.find_element(*self.CROP_AVATAR_FORM)))


