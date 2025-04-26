
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
driver.get("https://www.facebook.com/")

def locate_by_tagname_demo():
    divs=driver.find_elements(By.TAG_NAME,'div')
    print(f"Type: {type(divs)} , length : {len(divs)}")
    print(f"example : {divs[0].text}")
locate_by_tagname_demo()