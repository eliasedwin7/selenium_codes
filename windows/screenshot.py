from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_options= Options()
chrome_options.add_argument("--headless")

exe_path=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=exe_path,options=chrome_options)
driver.get("https://www.facebook.com/")

def get_webelement_property():
    web_element=driver.find_element(By.XPATH,"//ul[@class='uiList localeSelectorList _2pid _509- _4ki _6-h _6-j _6-i']")
    print(f"Text : {web_element.text} \n\n")
    print(f"class : {web_element.get_attribute('class')} \n\n")
    print(f"State: {web_element.is_enabled()}")
    web_element.screenshot("screenshots/test.png")
    driver.get_screenshot_as_file("screenshots/full.png")
  

get_webelement_property()
# Close the browser
driver.quit()