from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Developer\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element_by_name("fName")
fname.send_keys("sid")
fname.send_keys(Keys.ENTER)

lname = driver.find_element_by_name("lName")
lname.send_keys("desai")
lname.send_keys(Keys.ENTER)

email = driver.find_element_by_name("email")
email.send_keys("sidcode@gmail.com")
email.send_keys(Keys.ENTER)

# submit = driver.find_element_by_css_selector("form button")
# submit.click()