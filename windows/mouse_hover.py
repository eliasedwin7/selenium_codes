from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

chrome_options= Options()
#chrome_options.add_argument("--headless")

exe_path=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=exe_path,options=chrome_options)
driver.get("https://www.yatra.com/react-home/flights")
parent_window=driver.current_window_handle
print(f"Current Window : {parent_window}")
driver.maximize_window()
time.sleep(2)
driver.execute_script("window.scrollBy(0, 250);")
time.sleep(2)
actions=ActionChains(driver)




def get_webelement_property():
    web_element=driver.find_element(By.XPATH, "//button[normalize-space()='Search']")
    print(f"Text : {web_element.text} \n\n")
    actions.move_to_element(web_element).click().perform()
    time.sleep(3)

#action.context_click( webelement).perform() -> right click

#action.double_click( webelement).perform() -> double click
"""
Move a slider from left to right
actions.drag_and_drop_by_offset(element, 60,0).perform()
actions.click_and_hold(element).move_by_offset(50,0).release().perform()



Drag and drop
actions.drag_and_drop(elem1,elem2).perform()
actions.drag_and_drop_by_offset(elem1,50,40).perform()

"""

get_webelement_property()
# Close the browser
driver.quit()

