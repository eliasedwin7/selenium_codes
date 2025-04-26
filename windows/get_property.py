
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_options=Options()
chrome_options.add_argument("--headless")

executable_path = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=executable_path,options=chrome_options)

driver.get("https://example.com")

element = driver.find_element(By.TAG_NAME, "h1")  # Or any other tag
print(dir(element))  # List everything the WebElement supports

driver.quit()
