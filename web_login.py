#username: sbobet888@gmail.com
#password: 123456789

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

path = r'C:\Users\ken25\OneDrive\Desktop\01_Python\web_scrabling\chromedriver.exe'
service = Service(path)

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

driver = webdriver.Chrome(service=service, options=options)
driver.get("http://178.128.125.82/login/") #open website
time.sleep(2)

element = driver.find_element(By.NAME, "username")
element.send_keys("sbobet888@gmail.com")
time.sleep(2)

element = driver.find_element(By.NAME, "password")
element.send_keys("123456789")
#element.send_keys(Keys.RETURN)
time.sleep(2)

element = driver.find_element(By.XPATH, "/html/body/div[2]/form/button")
element.click()
time.sleep(2)

driver.get("http://178.128.125.82/sensor/")
time.sleep(2)
element = driver.find_element(By.NAME, "sid")
element.send_keys("ss")
element.send_keys(Keys.RETURN)

time.sleep(3)
temp = driver.find_element(By.CLASS_NAME, "temp")
humid = driver.find_element(By.CLASS_NAME, "humid")
print(temp.text)
print(humid.text)

time.sleep(10)

driver.close()