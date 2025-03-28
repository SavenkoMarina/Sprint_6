from allure import title

from data import urls
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestQuestions:
    @title("Проверка открытия первого вопроса")
    def test_first_question(self, driver):
        page = MainPage(driver)
        page.open_question_and_check_answer(
            MainPageLocators.FIRST_QUESTION,
            MainPageLocators.FIRST_ANSWER
        )

    @title("Проверка открытия второго вопроса")
    def test_second_question(self, driver):
        page = MainPage(driver)
        page.open_question_and_check_answer(
            MainPageLocators.SECOND_QUESTION,
            MainPageLocators.SECOND_ANSWER
        )

    @title("Проверка открытия третьего вопроса")
    def test_third_question(self, driver):
        page = MainPage(driver)
        page.open_question_and_check_answer(
            MainPageLocators.THIRD_QUESTION,
            MainPageLocators.THIRD_ANSWER
        )

    @title("Проверка открытия четвертого вопроса")
    def test_fourth_question(self, driver):
        page = MainPage(driver)
        page.open_question_and_check_answer(
            MainPageLocators.FOURTH_QUESTION,
            MainPageLocators.FOURTH_ANSWER
        )

    @title("Проверка открытия пятого вопроса")
    def test_fifth_question(self, driver):
        page = MainPage(driver)
        page.open_question_and_check_answer(
            MainPageLocators.FIFTH_QUESTION,
            MainPageLocators.FIFTH_ANSWER
        )

    @title("Проверка открытия шестого вопроса")
    def test_sixth_question(self, driver):
        page = MainPage(driver)
        page.open_question_and_check_answer(
            MainPageLocators.SIXTH_QUESTION,
            MainPageLocators.SIXTH_ANSWER
        )

    @title("Проверка открытия седьмого вопроса")
    def test_seventh_question(self, driver):
        page = MainPage(driver)
        page.open_question_and_check_answer(
            MainPageLocators.SEVENTH_QUESTION,
            MainPageLocators.SEVENTH_ANSWER
        )

    @title("Проверка открытия восьмого вопроса")
    def test_eighth_question(self, driver):
        page = MainPage(driver)
        page.open_question_and_check_answer(
            MainPageLocators.EIGHTH_QUESTION,
            MainPageLocators.EIGHTH_ANSWER
        )

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
