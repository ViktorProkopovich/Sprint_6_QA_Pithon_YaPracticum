import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver   
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открыть главную страницу")
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Поиск и ожидание элемента")
    def find_and_wait_locator(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))
    
    @allure.step("Ожидание появления элемента")
    def wait_for_element(self, locator, timeout=10):
        return self.wait.until(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
    
    @allure.step("Кликнуть по элементу")
    def click_on_locator(self, locator):
        self.find_and_wait_locator(locator).click()

    @allure.step("Ввод данных в поле")
    def send_keys_to_field(self, locator, text):
        self.find_and_wait_locator(locator).send_keys(text)

    @allure.step("Получить текст элемента")
    def get_element_text(self, locator):
        return self.find_and_wait_locator(locator).text
    
    @allure.step("Скроллинг до элемента")
    def scroll_to_locator(self, locator):
        element = self.find_and_wait_locator(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Перейти на другую вкладку')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        