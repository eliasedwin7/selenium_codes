from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.yatra.com/")
driver.maximize_window()
time.sleep(5)  # Wait for page and field to be ready

def get_departure_suggestions():
    input_box = driver.find_element(By.XPATH, "//div[@aria-label='Departure From New Delhi inputbox']")
    input_box.click()
    input_box = driver.find_element(By.ID, "input-with-icon-adornment")
    input_box.send_keys("AUS")
    time.sleep(10)  # Wait for suggestions to appear

    results = driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-134xwrj']//li[@class='css-1546kn3']")

    print("Suggestions:")
    for result in results:
        print(result.text)

get_departure_suggestions()

driver.quit()
