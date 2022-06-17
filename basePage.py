from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        spinner = By.XPATH, "//img[@alt='spinner']"
        WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located(spinner))
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(by_locator)).click()

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_elements_text(self, by_locator):
        return self.driver.find_elements(*by_locator)

    def switch_the_tab(self, handle):
        self.driver.switch_to.window(self.driver.window_handles[handle])

    def page_back(self):
        self.driver.back()

    def close_current_tab(self):
        self.driver.close()

    def get_url(self, url):
        self.driver.get(url)

    def scrollele(self, by_locator):
        element = self.driver.find_element(*by_locator)
        self.driver.execute_script("return arguments[0].scrollIntoView();", element)

    def scroll_by_pixel(self, value):
        self.driver.execute_script(f'window.scrollBy(0, '+value+')')
