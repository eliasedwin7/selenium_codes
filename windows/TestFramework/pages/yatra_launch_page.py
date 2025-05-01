from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver

class LaunchPage(BaseDriver):
    def __init__(self,driver,wait):
        super().__init__(driver)
        self.driver=driver
        self.wait=wait
    def search_depart_location(self,depart_location):
            input_box = self.driver.find_element(By.XPATH, "//div[@aria-label='Departure From New Delhi inputbox']")
            depart_from=self.wait_unitil_element_is_clickable(By.XPATH, "//div[@aria-label='Departure From New Delhi inputbox']")
            depart_from.click()
            input_box = self.driver.find_element(By.ID, "input-with-icon-adornment")
            input_box.send_keys(depart_location)

    def search_arival_location(self,depart_location):
            input_box = self.driver.find_element(By.XPATH, "//div[@aria-label='Going To Mumbai inputbox']")
            arive_to=self.wait_unitil_element_is_clickable(By.XPATH, "//div[@aria-label='Going To Mumbai inputbox']")
            arive_to.click()
            input_box = self.driver.find_element(By.ID, "input-with-icon-adornment-label")
            input_box.send_keys(depart_location)