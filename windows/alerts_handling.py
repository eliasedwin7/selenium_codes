from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

chrome_options= Options()
#chrome_options.add_argument("--headless")

exe_path=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=exe_path,options=chrome_options)
driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
parent_window=driver.current_window_handle
print(f"Current Window : {parent_window}")
driver.maximize_window()
time.sleep(2)
driver.execute_script("window.scrollBy(0, 250);")
time.sleep(2)




def get_webelement_property():
    driver.switch_to.frame("iframeResult")
    web_element=driver.find_element(By.TAG_NAME, "button")
    print(f"Text : {web_element.text} \n\n")
    web_element.click()
    time.sleep(3)
    driver.switch_to.alert.accept()
    time.sleep(3)

    web_element.click()
    time.sleep(3)
    driver.switch_to.alert.dismiss()
    time.sleep(3)
    """
    web_element.click()
    time.sleep(3)
    driver.switch_to.alert.send_keys("Add")
    driver.switch_to.alert.accept()
    """

    time.sleep(3)





get_webelement_property()
# Close the browser
driver.quit()

