import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from src.base_test import BaseTest
from utils.helpers import login
from selenium.webdriver.common.by import By
import time

class TestSocialMedia(BaseTest):
    def test_post_update(self):
        # Fetch login details from config
        with open('config/config.json') as config_file:
            config = json.load(config_file)

        login(self.driver, config['username'], config['password'])

        # Post an update
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//textarea[@name='xhpc_message']").send_keys("Automated post via Selenium")
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Post')]").click()

        # Verify the post was made
        assert "Automated post via Selenium" in self.driver.page_source
