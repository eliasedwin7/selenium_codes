from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.add_argument("--headless")  # run without UI

print("Launching Firefox...")
driver = webdriver.Firefox(options=options)
print("Opened browser")

driver.get("https://example.com")
print("Navigated to site")

print("Title:", driver.title)

driver.quit()
print("Closed browser")
