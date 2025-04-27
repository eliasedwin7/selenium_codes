from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.yatra.com/")
driver.maximize_window()

def get_departure_suggestions():
    input_box = driver.find_element(By.XPATH, "//div[@aria-label='Departure From New Delhi inputbox']")
    wait=WebDriverWait(driver,10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Departure From New Delhi inputbox']"))).click()
    #input_box.click()
    input_box = driver.find_element(By.ID, "input-with-icon-adornment")
    input_box.send_keys("AUS")

    


    results = driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-134xwrj']//li[@class='css-1546kn3']")

    print("Suggestions:")
    for result in results:
        print(result.text)

get_departure_suggestions()

driver.quit()
