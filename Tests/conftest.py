import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome", "firefox"])
def setup_teardown(request):
    global driver
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.quit()
