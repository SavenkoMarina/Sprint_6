import pytest
from allure import title

from data import urls
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestQuestions:

    @pytest.mark.parametrize(
        "question, answer",
        [
            (MainPageLocators.FIRST_QUESTION, MainPageLocators.FIRST_ANSWER),
            (MainPageLocators.SECOND_QUESTION, MainPageLocators.SECOND_ANSWER),
            (MainPageLocators.THIRD_QUESTION, MainPageLocators.THIRD_ANSWER),
            (MainPageLocators.FOURTH_QUESTION, MainPageLocators.FOURTH_ANSWER),
            (MainPageLocators.FIFTH_QUESTION, MainPageLocators.FIFTH_ANSWER),
            (MainPageLocators.SIXTH_QUESTION, MainPageLocators.SIXTH_ANSWER),
            (MainPageLocators.SEVENTH_QUESTION, MainPageLocators.SEVENTH_ANSWER),
            (MainPageLocators.EIGHTH_QUESTION, MainPageLocators.EIGHTH_ANSWER),
        ]
    )
    @title("Проверка открытия вопроса")
    def test_first_question(self, driver, question, answer):
        page = MainPage(driver)
        page.open_question_and_check_answer(question, answer)

    @title('Клик на логотип "Самокат"')
    def test_click_logo_scooter(self, driver):
        page = MainPage(driver)
        page.wait_for_clickable_element(MainPageLocators.LOGO_SCOOTER)
        page.click_element(MainPageLocators.LOGO_SCOOTER)
        assert driver.current_url == urls.MAIN_URL


    @title('Клик на логотип "Яндекс"')
    def test_click_logo_yandex(self, driver):
        page = MainPage(driver)
        page.wait_for_clickable_element(MainPageLocators.LOGO_YANDEX)
        page.click_element(MainPageLocators.LOGO_YANDEX)

        page.switch_to_the_second_tab()
        page.wait_for_load_element(MainPageLocators.DZEN_BODY)
        assert urls.YANDEX_LOGO_URL in driver.current_url
