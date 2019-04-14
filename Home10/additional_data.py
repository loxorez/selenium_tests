import random
import string


def random_string(string_min_len, string_max_len):
    """
    Create a string using random characters
    :param string_min_len: string is expected to be generated in range from min value
    :param string_max_len: string is expected to be generated in range to max value
    :return: string with random cases characters
    """
    ascii_let_dig = string.ascii_letters + string.digits
    string_result = "".join(random.choices(ascii_let_dig, k=random.randint(string_min_len, string_max_len)))
    return string_result


class presence_num_of_elements:
    def __init__(self, locator, number):
        self.locator = locator
        self.number = number

    def __call__(self, driver):
        elements = driver.find_elements(*self.locator)
        if len(elements) == self.number:
            return elements

