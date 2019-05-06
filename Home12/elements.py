from selenium.webdriver.common.by import By
from models.user import User
from selenium.common.exceptions import NoSuchElementException


class StatusNewsfeedBody(object):
    """Status newsfeed body elements placed here"""
    STATUS_ADDED_TIME = (By.CLASS_NAME, "ow_newsfeed_date")
    STATUS_USER = (By.CSS_SELECTOR, ".ow_newsfeed_string.ow_small > a")
    STATUS = (By.CLASS_NAME, 'ow_newsfeed_content')
    STATUS_MORE_BUTTON = (By.LINK_TEXT, 'See more')
    LIKE_COUNTER = (By.CLASS_NAME, "newsfeed_counter_likes")
    LIKE_STRING = (By.CLASS_NAME, "newsfeed_likes_string")
    STATUS_COUNTER = (By.CLASS_NAME, "newsfeed_counter_comments")
    INSIDE_STATUS = (By.CLASS_NAME, "ow_comments_item")

    def __init__(self, web_element):
        self.web_element = web_element

    # @property
    # def text(self):
    # # Click see more if it present in status, return full text
    #     try:
    #         see_more_element = self.web_element.find_element(*self.STATUS_MORE_BUTTON)
    #         see_more_element.click()
    #         return self.web_element.find_element(*self.STATUS).text
    #     except NoSuchElementException as e:
    #         return self.web_element.find_element(*self.STATUS).text

    @property
    def text(self):
        # Status text
        return self.web_element.find_element(*self.STATUS).text

    @property
    def time(self):
        # Time since status was added
        return self.web_element.find_element(*self.STATUS_ADDED_TIME).text

    @property
    def likes_value(self):
        # Status likes value
        return int(self.web_element.find_element(*self.LIKE_COUNTER).text)

    @property
    def like_string(self):
        # Like string (username who liked status)
        return self.web_element.find_element(*self.LIKE_STRING).text

    @property
    def status_value(self):
        # Comments value which placed inside status
        return int(self.web_element.find_element(*self.STATUS_COUNTER).text)

    @property
    def user(self):
        # Status created user data
        user_element = self.web_element.find_element(*self.STATUS_USER)
        return User(
            username = user_element.get_attribute("href").split("/")[-1],
            real_name = user_element.text
        )

    @property
    def inner_statuses(self):
        # Return inner statuses forms
        return self.web_element.find_elements(*self.INSIDE_STATUS)


class InputTextElement(object):
    """Input newsfeed text area elements placed here"""
    def __init__(self, web_element):
        self.web_element = web_element

    @property
    def placeholder(self):
        """Return text that located in the input field"""
        return self.web_element.get_attribute("placeholder")


class WelcomeWidget(object):
    """WelcomeWidget elements placed here"""
    TITLE_STRING = (By.CLASS_NAME, "ow_ic_warning")
    WIDGET_STRING = (By.CLASS_NAME, "oow_custom_html_widget")
    SETTINGS = (By.CLASS_NAME, "ow_ic_gear_wheel")
    DELETE = (By.CLASS_NAME, "ow_ic_delete")

    def __init__(self, web_element):
        self.web_element = web_element

    @property
    def title_text(self):
        # Warning text
        return self.web_element.find_element(*self.TITLE_STRING).text

    @property
    def widget_text(self):
        # Warning text
        return self.web_element.find_element(*self.WIDGET_STRING).text

    @property
    def settings_button(self):
        # Settings button
        return self.web_element.find_element(*self.SETTINGS)

