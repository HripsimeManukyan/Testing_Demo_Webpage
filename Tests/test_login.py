from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("setup_teardown")
class TestLogin:

    @pytest.mark.smoke
    def test_login_with_valid_inputs(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").send_keys("arun9@gmail.com")
        self.driver.find_element(By.ID, "input-password").send_keys("12345")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        assert self.driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()

    @pytest.mark.regression
    def test_login_without_inputs(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").send_keys("")
        self.driver.find_element(By.ID, "input-password").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        expected_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH,
                                        "//div[@class='alert alert-danger alert-dismissible']").text.__contains__(
            expected_message)
