from allure import step
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from data import urls

class Orders(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.go_to_url(urls.ORDER_URL)
        self.wait_for_load_element(OrderPageLocators.NAME_FIELD)

    @step("Заполяем первую часть формы")
    def fill_first_step(self, name, surname, address, phone):
        self.input_to_element(OrderPageLocators.NAME_FIELD, name)
        self.input_to_element(OrderPageLocators.SURNAME_FIELD, surname)
        self.input_to_element(OrderPageLocators.ADDRESS_FIELD, address)
        self.input_to_element(OrderPageLocators.PHONE_FIELD, phone)

        self.click_element(OrderPageLocators.METRO_INPUT)
        self.wait_for_clickable_element(OrderPageLocators.METRO_STATION)
        self.click_element(OrderPageLocators.METRO_STATION)

    @step("Заполяем вторую часть формы")
    def fill_second_step(self, comment):
        self.click_element(OrderPageLocators.DELIVERY_DATE_CALENDAR)
        self.wait_for_clickable_element(OrderPageLocators.DATE_DELIVERY_CHOICE)
        self.click_element(OrderPageLocators.DATE_DELIVERY_CHOICE)

        self.click_element(OrderPageLocators.RENTAL_PERIOD_INPUT)
        self.wait_for_clickable_element(OrderPageLocators.PERIOD_DAYS)
        self.click_element(OrderPageLocators.PERIOD_DAYS)

        self.click_element(OrderPageLocators.COLOR_BLACK_CHECKBOX)

        self.input_to_element(OrderPageLocators.COMMENT_FIELD, comment)
        self.click_element(OrderPageLocators.FORM_ORDER_BTN)

        self.wait_for_clickable_element(OrderPageLocators.YES_BTN)
        self.click_element(OrderPageLocators.YES_BTN)

        self.wait_for_clickable_element(OrderPageLocators.STATUS_BTN)
        self.click_element(OrderPageLocators.STATUS_BTN)



