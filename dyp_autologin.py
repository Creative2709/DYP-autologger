#from logging import error
#from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

# Login credentials
with open('creds.txt', 'r') as f:
    lines = f.readlines()

print(lines)    
    
username = lines[0]
password = lines[1]

# initialize the Chrome driver
driver = webdriver.Chrome(r"driverfile\chromedriver.exe")
# head to  login page
driver.get("http:192.168.25.1:8090")


# find username/email field and send the username itself to the input field
driver.find_element_by_id("username").send_keys(username)
# find password input field and insert password
driver.find_element_by_id("password").send_keys(password)
# click login button

driver.find_element_by_id("loginbutton").click()

# # close the driver
driver.close()
driver.quit()