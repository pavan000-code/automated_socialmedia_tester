from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


class BaseTest:
    def setup_method(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        
        service = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())




        self.driver = webdriver.Chrome(service=service, options=chrome_options)

        # Implicit wait for elements
        self.driver.implicitly_wait(10)

    def teardown_method(self):
        # Close the browser after the test
        self.driver.quit()

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
