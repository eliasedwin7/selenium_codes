import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

executable_path = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=executable_path)
driver.get("https://www.facebook.com/")

def locate_by_id_demo():
    driver.find_element(By.ID,'email').send_keys('sample@sample')
    time.sleep(4)

def locate_by_name_demo():
    driver.find_element(By.NAME,'pass').send_keys('sample')
    time.sleep(4)
locate_by_id_demo()
locate_by_name_demo()
