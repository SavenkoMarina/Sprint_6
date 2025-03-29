import pytest
from data import urls

from allure import title
from pages.main_page import MainPage

from pages.order_page import Orders
from data.urls import ORDER_URL
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators

class TestOrder:
    @title("Проверка перехода из шапки")
    def test_go_to_order_from_head(self, driver):
        page = MainPage(driver)
        page.wait_for_clickable_element(MainPageLocators.ORDER_BTN_HEAD)
        page.click_element(MainPageLocators.ORDER_BTN_HEAD)

        page.wait_for_load_element(OrderPageLocators.NAME_FIELD)
        assert driver.current_url == ORDER_URL

    @title("Проверка перехода из подвала")
    def test_go_to_order_from_footer(self, driver):
        page = MainPage(driver)
        page.wait_for_clickable_element(MainPageLocators.ORDER_BTN_HEAD)
        page.scroll_to_element(MainPageLocators.ORDER_BTN_FOOTER)
        page.click_element(MainPageLocators.ORDER_BTN_FOOTER)

        page.wait_for_load_element(OrderPageLocators.NAME_FIELD)
        assert driver.current_url == ORDER_URL

    @pytest.mark.parametrize("step1_data, comment", [
        (
                {'name': 'Светлана', 'surname': 'Мендельсон', 'address': 'ул. Пушкина, д. 17',
                 'phone': '+7913689552'},
                'Спасибо!!111!!!'
        ),
        (
                {'name': 'Павел', 'surname': 'Павлов', 'address': 'ул. Лишняя, д6',
                 'phone': '+7910031337'},
                'Если что, спросите Павла'
        )
    ])
    @title("Проверка создания заказа")
    def test_order(self, driver, step1_data, comment):
        page = Orders(driver)
        page.fill_first_step(
            step1_data["name"],
            step1_data["surname"],
            step1_data["address"],
            step1_data["phone"],
        )
        page.click_element(OrderPageLocators.NEXT_BTN)

        page.wait_for_load_element(OrderPageLocators.DELIVERY_DATE_CALENDAR)
        page.fill_second_step(comment)

        page.wait_for_load_element(MainPageLocators.LOGO_YANDEX)
        assert urls.TRACK_URL in driver.current_url