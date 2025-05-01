from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest



@pytest.fixture(scope="class")
def setup(request):
    chrome_options = Options()

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    wait=WebDriverWait(driver,10)
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver=driver
    request.cls.wait=wait
    yield
    driver.close()