import allure
from data import Urls
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = Urls.PAGE_MAIN

    @allure.step("Принять куки")
    def accept_cookies(self):
        try:
            self.click_on_locator(MainPageLocators.BTN_COOKIES)
        except Exception:
            pass

    @allure.step("Клик по кнопке 'Заказать' вверху страницы")
    def click_btn_order_up(self):
        self.click_on_locator(MainPageLocators.BTN_ORDER_UP)

    @allure.step("Клик по кнопке 'Заказать' внизу страницы")
    def click_btn_order_low(self):
        self.scroll_to_locator(MainPageLocators.BTN_ORDER_LOW)
        self.click_on_locator(MainPageLocators.BTN_ORDER_LOW)

    @allure.step("Клик на вопрос № {q_number}")
    def expand_faq_qq(self, q_number):
        
        questions = [
            MainPageLocators.QQ_1,
            MainPageLocators.QQ_2, 
            MainPageLocators.QQ_3,
            MainPageLocators.QQ_4,
            MainPageLocators.QQ_5,
            MainPageLocators.QQ_6,
            MainPageLocators.QQ_7,
            MainPageLocators.QQ_8
        ]
        self.scroll_to_locator(questions[q_number])
        self.click_on_locator(questions[q_number])

    @allure.step("Получить ответ №{ans_number}")
    def get_faq_ans(self, ans_number):
        ans = [
            MainPageLocators.ANS_1,
            MainPageLocators.ANS_2,
            MainPageLocators.ANS_3,
            MainPageLocators.ANS_4,
            MainPageLocators.ANS_5,
            MainPageLocators.ANS_6,
            MainPageLocators.ANS_7,
            MainPageLocators.ANS_8
        ]
        return self.get_element_text(ans[ans_number])
    
    @allure.step("Клик по лого 'Яндекс'")
    def click_yandex_logo(self):
        self.click_on_locator(OrderPageLocators.LOGO_YA)


    @allure.step("Клик по лого 'Самокат'")
    def click_scooter_logo(self):
        self.click_on_locator(OrderPageLocators.LOGO_SC)
