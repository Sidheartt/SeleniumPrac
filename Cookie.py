from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Developer\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_id("cookie")

for i in range(100):
    cookie.click()

