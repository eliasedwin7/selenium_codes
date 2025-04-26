from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time

chrome_options= Options()

exe_path=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=exe_path,options=chrome_options)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select")
def get_webelement_property():
    web_element=driver.find_element(By.ID,"cars")
    dropdown_select=Select(web_element)
    dropdown_select.select_by_index(1)
    time.sleep(3)
    dropdown_select.select_by_visible_text("Saab")
    time.sleep(3)
    dropdown_select.select_by_value("audi")
    time.sleep(3)
    # Close the browser


get_webelement_property()
driver.quit()

