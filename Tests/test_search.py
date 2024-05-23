import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_teardown")
class TestSearch:

    @pytest.mark.smoke
    def test_search_with_valid_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("HP")
        search_button = self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']")
        search_button.click()

        element_to_scroll_to = self.driver.find_element(By.LINK_TEXT, "HP LP3065")
        self.driver.execute_script("arguments[0].scrollIntoView();", element_to_scroll_to)
        assert element_to_scroll_to.is_displayed()
        assert self.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()

    @pytest.mark.regression
    def test_search_with_invalid_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("BMW")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        expected_text = "There is no product that matches the search criteria."
        actual_text_element = self.driver.find_element(By.XPATH,
                                                       "//p[contains(text(),'There is no product that matches the search criter')]")
        assert actual_text_element.text == expected_text

    @pytest.mark.sanity
    def test_search_without_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        expected_text = "There is no product that matches the search criteria."
        actual_text_element = self.driver.find_element(By.XPATH,
                                                       "//p[contains(text(),'There is no product that matches the search criter')]")
        assert actual_text_element.text == expected_text
