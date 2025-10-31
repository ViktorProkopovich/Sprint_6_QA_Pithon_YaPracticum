import allure
from data import Urls
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators

class TestLogo:

    @allure.title("Проверка перехода на главную страницу по логотипу 'Самокат'")
    def test_click_sc_logo_redirects_main(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        driver.get(Urls.PAGE_ORDER)
        main_page.click_scooter_logo()

        assert Urls.PAGE_MAIN in driver.current_url

    @allure.title("Проверка перехода на страницу 'Dzen' по логотипу 'Яндекс'")
    def test_click_ya_logo_redirects_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_yandex_logo()
        main_page.switch_to_next_tab()
        main_page.wait_for_element(MainPageLocators.DZEN)
        current_url = driver.current_url
        assert Urls.PAGE_DZEN in current_url
        