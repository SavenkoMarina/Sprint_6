from allure import step
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

TIMEOUT = 5

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_url(self, url):
        self.driver.get(url)

    def wait_for_load_element(self, locator):
        WebDriverWait(self.driver,TIMEOUT).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def wait_for_clickable_element(self, locator):
        WebDriverWait(self.driver, TIMEOUT).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        return self.driver.find_element(*locator).click()

    def input_to_element(self, locator, data):
        return self.driver.find_element(*locator).send_keys(data)

    def scroll_to_element(self, locator):
        return self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            self.find_element(locator)
        )

    def switch_to_the_second_tab(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])