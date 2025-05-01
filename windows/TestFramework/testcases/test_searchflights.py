from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.usefixtures("setup")
class TestsearchandVerfiy():
    def test_get_departure_suggestions(self):
        input_box = self.driver.find_element(By.XPATH, "//div[@aria-label='Departure From New Delhi inputbox']")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Departure From New Delhi inputbox']"))).click()
        #input_box.click()
        input_box = self.driver.find_element(By.ID, "input-with-icon-adornment")
        input_box.send_keys("AUS")

        results = self.driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-134xwrj']//li[@class='css-1546kn3']")

        print("Suggestions:")
        for result in results:
            print(result.text)


