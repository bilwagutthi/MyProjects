import time
from selenium import webdriver

driver = webdriver.Firefox()
# Maximize the browser window
driver.maximize_window()
# Navigate to LinkedIn page
driver.get("https://www.linkedin.com/")

 
signinbutton = driver.find_element_by_xpath('//a[@class="nav__button-secondary"]')  
signinbutton.click()
# Wait for the new page to load
time.sleep(3)
# Verify user is Sign_In page
try:
    driver.find_element_by_xpath('//h1[@class="header__content__heading"]')
except Exception as e:
    #This pattern of catching all exceptions is ok when you are starting out
    result_flag = False 
else:
    result_flag = True
if result_flag is True:
    print("Sucess:Directing to sign in page")
else:
    print("Unsuccesful:Directing to sign in page")

#Enter text 
tbUserName=driver.find_element_by_xpath('//input[@id="username"]')
tbUserName.send_keys("Bilwa")
tbPassword=driver.find_element_by_xpath('//input[@id="password"]')
tbPassword.send_keys("Bilwa")
time.sleep(3)


# Close the browser   
driver.close()