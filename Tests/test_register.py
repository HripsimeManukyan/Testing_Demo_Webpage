from selenium.webdriver.common.by import By
import pytest
import time


def generate_email_time_stamp():
    timestamp = time.strftime("%Y%m%d%H%M%S")
    return f"alice{timestamp}@gmail.com"


@pytest.mark.usefixtures("setup_teardown")
class TestRegister:
    @pytest.mark.smoke
    def test_register(self):
        self.driver.find_element(By.XPATH, "//ul[@class='list-inline']//li[@class='dropdown']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.XPATH, "//input[@id='input-firstname']").send_keys("Alice")
        self.driver.find_element(By.XPATH, "//input[@id='input-lastname']").send_keys("Brown")

        email = generate_email_time_stamp()
        self.driver.find_element(By.ID, "input-email").send_keys(email)
        self.driver.find_element(By.ID, "input-telephone").send_keys("78956123")
        self.driver.find_element(By.ID, "input-password").send_keys("testing")
        self.driver.find_element(By.ID, "input-confirm").send_keys("testing")
        self.driver.find_element(By.XPATH, "//label[normalize-space()='Yes']//input[@name='newsletter']").click()
        self.driver.find_element(By.XPATH, "//input[@name='agree']").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()

        expected_message = "Your Account Has Been Created!"
        actual_message = self.driver.find_element(By.XPATH,
                                                  "//h1[normalize-space()='Your Account Has Been Created!']").text
        assert actual_message == expected_message

    @pytest.mark.regression
    def test_register_without_agree_policy(self):
        self.driver.find_element(By.XPATH, "//ul[@class='list-inline']//li[@class='dropdown']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.XPATH, "//input[@id='input-firstname']").send_keys("Alice")
        self.driver.find_element(By.XPATH, "//input[@id='input-lastname']").send_keys("Brown")

        email = generate_email_time_stamp()
        self.driver.find_element(By.ID, "input-email").send_keys(email)
        self.driver.find_element(By.ID, "input-telephone").send_keys("78956123")
        self.driver.find_element(By.ID, "input-password").send_keys("testing")
        self.driver.find_element(By.ID, "input-confirm").send_keys("testing")
        self.driver.find_element(By.XPATH, "//label[normalize-space()='Yes']//input[@name='newsletter']").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()

        expected_message = "Warning: You must agree to the Privacy Policy!"
        actual_message = self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text
        assert expected_message in actual_message
