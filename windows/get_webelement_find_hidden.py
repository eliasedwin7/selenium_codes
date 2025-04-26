from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_options= Options()
chrome_options.add_argument("--headless")


exe_path=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=exe_path,options=chrome_options)
driver.get("https://www.w3schools.com/HOWTO/howto_js_toggle_hide_show.asp")

def get_webelement_property():
    web_element=driver.find_element(By.XPATH,"//div[@id='myDIV']")
    print(f"Text : {web_element.text} \n\n")
    print(f"State: {web_element.is_displayed()}")

    driver.find_element(By.XPATH,"//button[normalize-space()='Toggle Hide and Show']").click()
    print(f"State: {web_element.is_displayed()}")



get_webelement_property()
# Close the browser
driver.quit()   