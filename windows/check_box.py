from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_options= Options()
#chrome_options.add_argument("--headless")

exe_path=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=exe_path,options=chrome_options)
driver.get("https://www.w3schools.com/HOWTO/howto_js_display_checkbox_text.asp")

def get_webelement_property():
    web_element=driver.find_element(By.XPATH,"//input[@id='myCheck']")
    print(f"Text : {web_element.text} \n\n")
    print(f"class : {web_element.get_attribute('class')} \n\n")
    print(f"State of checkbox : {web_element.is_selected()}")
    web_element.click()
    flag=driver.find_element(By.XPATH,"//p[@id='text']").is_displayed()
    print(f"checkbox displayed: {flag}")
    web_element.click()
    flag=driver.find_element(By.XPATH,"//p[@id='text']").is_displayed()
    print(f"checkbox displayed: {flag}")
  

get_webelement_property()
# Close the browser
driver.quit()