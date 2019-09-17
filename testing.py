import time
from selenium import webdriver

driver = webdriver.Firefox()
# Maximize the browser window
driver.maximize_window()
# Navigate to LinkedIn page
driver.get("https://www.linkedin.com/")
#Find Sign In button
signinbutton = driver.find_element_by_xpath('//a[@class="nav__button-secondary"]')
#Click Sign In button  
signinbutton.click()
# Wait for the new page to load
time.sleep(3)
# Verify user is Sign_In page

if driver.title == "LinkedIn Login, Sign in | LinkedIn":
    print("Sucess:Directing to sign in page")
else:
    print("Unsuccesful:Directing to sign in page")

#Enter Username field and enter text
tbUserName=driver.find_element_by_xpath('//input[@id="username"]')
tbUserName.send_keys("Username")
#Enter Username field and enter text
tbPassword=driver.find_element_by_xpath('//input[@id="password"]')
tbPassword.send_keys("Password")

time.sleep(3)

# Close the browser   
driver.close()