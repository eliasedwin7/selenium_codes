
"""
find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "xpath")
find_element(By.LINK_TEXT, "link text")
find_element(By.PARTIAL_LINK_TEXT, "partial link text")
find_element(By.TAG_NAME, "tag name")
find_element(By.CLASS_NAME, "class name")
find_element(By.CSS_SELECTOR, "css selector")

"""


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
locate_by_id_demo()

def locate_by_name_demo():
    driver.find_element(By.NAME,'pass').send_keys('sample')
    time.sleep(4)
locate_by_name_demo()

def locate_by_xpath_demo():
    driver.find_element(By.XPATH,"//input[@id='email']").send_keys('sample')
    time.sleep(4)
locate_by_xpath_demo()


def locate_by_cssselector_demo():
    driver.find_element(By.CSS_SELECTOR,"#pass").send_keys('sample')
    time.sleep(4)
locate_by_cssselector_demo()


def locate_by_tagname_demo():
    driver.find_element(By.TAG_NAME,"button").click()
    time.sleep(10)
locate_by_tagname_demo()
