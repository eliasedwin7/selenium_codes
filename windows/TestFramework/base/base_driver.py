import time
from selenium.webdriver.support import expected_conditions as EC

class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        
        while True:
            # Scroll to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)  # Wait for page to load

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def wait_for_presence_of_all_elements(self,locator_type,locator):
        allstops=self.wait.unit(EC.presence_of_all_eleemets_located((locator_type,locator)))
        return allstops

    def wait_unitil_element_is_clickable(self,locator_type,locator):
        element=self.wait.until(EC.element_to_be_clickable((locator_type,locator)))
        return element