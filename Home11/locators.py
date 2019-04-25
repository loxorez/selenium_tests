from selenium.webdriver.common.by import By


class DefaultPageLocators(object):
    """Class for default, guest page locators."""
    SIGN_IN = (By.CLASS_NAME, "ow_signin_label")
    SIGN_UP = (By.CLASS_NAME, "ow_console_item_link")


class SignInPageLocators(object):
    """Class for login page locators."""
    LOGIN_WINDOW = (By.CLASS_NAME, "floatbox_container")
    USER_NAME = (By.NAME, "identity")
    PASSWORD = (By.NAME, "password")
    SUBMIT = (By.NAME, "submit")
    REMEMBER_BOX = (By.NAME, "remember")


class DashboardPageLocators(object):
    """Class for dashboard page locators."""
    STATUS = (By.CLASS_NAME, 'ow_newsfeed_content')
    STATUS_ADD_FORM = (By.NAME, "status")
    STATUS_SUBMIT = (By.NAME, "save")
    STATUS_MORE_BUTTON = (By.LINK_TEXT, 'See more')
    STATUS_CONTEXT = (By.CLASS_NAME, "ow_context_more")
    STATUS_DELETE = (By.CLASS_NAME, "newsfeed_remove_btn")
    USER_PROFILE = (By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div[5]/a')
    SIGN_OUT = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div/div[5]/div/div/div[2]/ul/li[7]/div/a")
    INFORM_MESSAGE = (By.CLASS_NAME, "ow_message_node")
    INFORM_MESSAGE_CLOSE = (By.CLASS_NAME, 'close_button')
    LIKE_COUNTER = (By.CLASS_NAME, "newsfeed_counter_likes")
    LIKE_STATUS = (By.CLASS_NAME, "ow_miniic_like")
    LIKE_STRIG = (By.CLASS_NAME, "newsfeed_likes_string")
    STATUS_COUNTER = (By.CLASS_NAME, "newsfeed_counter_comments")
    STATUS_FORM = (By.CLASS_NAME, "ow_comments_form_wrap")
    STATUS_INSIDE_BUTTON = (By.CLASS_NAME, "ow_miniic_comment")
    STATUS_INSIDE_COMMENT_FORM = (By.CLASS_NAME, "comments_fake_autoclick")
    STATUS_ADDED_TIME = (By.CLASS_NAME, "ow_newsfeed_date")

