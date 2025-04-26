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
driver.get("https://www.yatra.com/")
parent_window=driver.current_window_handle
print(f"Current Window : {parent_window}")
driver.maximize_window()
time.sleep(2)
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(2)



def get_webelement_property():
    web_element=driver.find_element(By.XPATH, "//div[contains(text(),'View all offers')]")
    print(f"Text : {web_element.text} \n\n")
    web_element.click()
    time.sleep(3)
    all_handles=driver.window_handles
    for handle in all_handles:
        if handle != parent_window:
            print(f"New Window : {handle}")
            driver.switch_to.window(handle)
            driver.find_element(By.XPATH,"//a[@href='https://www.yatra.com/offer/details/sbi-credit-card-emi-offers']//span[@class='wfull offer-content anim']//span[@class='details wfull bxs']//span[@class='flL view mt10']//span[@class='view-btn flR anim'][normalize-space()='View Details']").click()
            time.sleep(4)
            break
        driver.switch_to.window(parent_window)
        time.sleep(4)




get_webelement_property()
# Close the browser
driver.quit()

