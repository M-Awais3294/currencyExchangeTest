import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    def assert_current_url(self, string):
        assert string in self.driver.current_url

    # def wait_for_element(self, element):
    #     WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located(self.driver.find_element(By.XPATH, element))
    #     )
