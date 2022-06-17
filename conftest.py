import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    global driver
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.set_page_load_timeout(20)

    if request.param == "firefox":
        driver = webdriver.Firefox()

    request.cls.driver = driver
    driver.maximize_window()

    yield
    driver.quit()
