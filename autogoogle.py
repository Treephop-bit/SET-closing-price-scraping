from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

path = r'C:\Users\ken25\OneDrive\Desktop\01_Python\web_scrabling\chromedriver.exe'
service = Service(path)



driver = webdriver.Chrome(service=service)
driver.get("http://www.google.com") #open website
element = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
element.send_keys("python")
element.send_keys(Keys.RETURN)

time.sleep(10)
element = driver.find_element(By.NAME, "q")
element.clear()
element.send_keys("thailand")
element.send_keys(Keys.RETURN)

time.sleep(10)

driver.close()