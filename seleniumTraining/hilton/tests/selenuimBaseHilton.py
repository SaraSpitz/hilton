from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
class seleniumBase():

    def selenium_start(self):
        print("start test")
        # options.add_argument("--headless") # Runs Chrome in headless mode.
        options = Options()
        options.headless = False
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver

    def selenium_end(self,driver):
        print ("selenium end")
        driver.close()