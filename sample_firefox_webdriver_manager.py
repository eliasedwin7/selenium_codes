from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

options = Options()
options.add_argument("--headless")  # Run in headless mode
options.set_preference("gfx.webrender.all", False)
options.set_preference("layers.acceleration.disabled", True)
options.set_preference("media.hardware-video-decoding.enabled", False)

print("Launching Firefox...")
service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)
print("Opened browser")

driver.get("https://example.com")
print("Navigated to site")

print("Title:", driver.title)

driver.quit()
print("Closed browser")
