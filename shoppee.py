from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

path = r'C:\Users\ken25\OneDrive\Desktop\01_Python\web_scrabling\chromedriver.exe'
service = Service(path)

driver = webdriver.Chrome(service=service)

web_url = 'https://cpfreshmartshop.com/%E0%B8%AB%E0%B8%A1%E0%B8%B9/%E0%B8%AB%E0%B8%A1%E0%B8%B9%E0%B8%AA%E0%B8%94'


products = driver.find_elements(By.CLASS_NAME, 'MuiBox-root css-r0hfyj')
print(products)

time.sleep(10)
driver.quit()