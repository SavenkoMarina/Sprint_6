from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FIELD = By.XPATH, "//input[@placeholder='* Имя']"
    SURNAME_FIELD = By.XPATH, "//input[@placeholder='* Фамилия']"
    ADDRESS_FIELD = By.XPATH, "//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN']"
    METRO_INPUT = By.XPATH, "//input[@class='select-search__input']"
    METRO_STATION = By.XPATH, "//div[text()='Сокольники']"
    PHONE_FIELD = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    NEXT_BTN = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    DELIVERY_DATE_CALENDAR = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    DATE_DELIVERY_CHOICE = By.XPATH, "//div[@class='react-datepicker__month']/div[@class='react-datepicker__week'][6]/div[7]"
    RENTAL_PERIOD_INPUT = By.XPATH, "//div[@class='Dropdown-root']"
    PERIOD_DAYS = By.XPATH, "//div[text()='двое суток']"
    SCOOTER_COLOR_LIST = By.XPATH, "//div[@class='Order_Title__3EKne']"
    COLOR_BLACK_CHECKBOX = By.XPATH, "//label[@for='black']"
    COMMENT_FIELD = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    FORM_ORDER_BTN = By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']"
    YES_BTN = By.XPATH, "//button[(text()='Да')]"
    STATUS_BTN = By.XPATH, "//button[(text()='Посмотреть статус')]"



