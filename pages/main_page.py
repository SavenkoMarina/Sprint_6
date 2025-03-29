from allure import step

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import urls

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.go_to_url(urls.MAIN_URL)
        self.wait_for_load_element(MainPageLocators.QUESTION_FIELD)

    @step("Открыть окно и проверить ответ")
    def open_question_and_check_answer(self, question_locator, answer_locator):
        self.scroll_to_element(MainPageLocators.QUESTION_FIELD)
        self.click_element(question_locator)
        self.wait_for_load_element(answer_locator)