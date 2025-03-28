from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_FIELD = (By.XPATH, "//div[@class='Home_FourPart__1uthg']")

    FIRST_QUESTION = (By.ID, "accordion__heading-0")
    FIRST_ANSWER = (By. ID, "accordion__panel-0")

    SECOND_QUESTION = (By.ID, "accordion__heading-1")
    SECOND_ANSWER = (By.ID, "accordion__panel-1")

    THIRD_QUESTION = (By.ID, "accordion__heading-2")
    THIRD_ANSWER = (By.ID, "accordion__panel-2")

    FOURTH_QUESTION = (By.ID, "accordion__heading-3")
    FOURTH_ANSWER = (By.ID, "accordion__panel-3")

    FIFTH_QUESTION = (By.ID, "accordion__heading-4")
    FIFTH_ANSWER = (By.ID, "accordion__panel-4")

    SIXTH_QUESTION = (By.ID, "accordion__heading-5")
    SIXTH_ANSWER = (By.ID, "accordion__panel-5")

    SEVENTH_QUESTION = (By.ID, "accordion__heading-6")
    SEVENTH_ANSWER = (By.ID, "accordion__panel-6")

    EIGHTH_QUESTION = (By.ID, "accordion__heading-7")
    EIGHTH_ANSWER = (By.ID, "accordion__panel-7")

    ORDER_BTN_HEAD = By.XPATH, "//button[@class='Button_Button__ra12g']"
    ORDER_BTN_FOOTER = By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button"

    LOGO_SCOOTER = By.XPATH, "//img[@alt='Scooter']//parent::a"
    LOGO_YANDEX = By.XPATH, "//img[@alt='Yandex']//parent::a"

    DZEN_BODY = By.XPATH, "//div[@id='root']"