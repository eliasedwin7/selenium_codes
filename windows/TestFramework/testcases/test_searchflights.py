from selenium.webdriver.common.by import By
import pytest
from pages.yatra_launch_page import LaunchPage
from base.base_driver import BaseDriver

@pytest.mark.usefixtures("setup")
class TestsearchandVerfiy():
    def test_get_departure_suggestions(self):
        lp=LaunchPage(self.driver,self.wait)
        lp.search_depart_location('AUS')
        results = self.driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-134xwrj']//li[@class='css-1546kn3']")
        #lp.going_to("")
        #lp.selectdate("24/08/2025")
        # lp.clicksearch()
        #lp.page_scroll
        #sf= SearchFlighResults(self.driver,self.wait)
        #sf.filter_flights()
        print("Suggestions:")
        for result in results:
            print(result.text)


    @pytest.mark.skip
    def test_get_arival_suggestions(self):
        lp=LaunchPage(self.driver,self.wait)
        lp.search_arival_location('COK')
        results = self.driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-134xwrj']//li[@class='css-1546kn3']")

        print("Suggestions:")
        for result in results:
            print(result.text)



