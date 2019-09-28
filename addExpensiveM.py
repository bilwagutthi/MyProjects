<<<<<<< HEAD
"""
This program is used to find the most expensive moisterizer and add it to the cart
"""

from selenium import webdriver
import time

# Creating an instence of thw web browser and navigating to the Shopping page
browser = webdriver.Firefox()
browser.get('https://weathershopper.pythonanywhere.com/')

# Checking if the right web page has been loaded
if browser.title!="The best moisturizers in the world!":
    print("Error in loading page")
    browser.close()
    exit()
else:
    print("Page loaded")



browser.close()
=======
"""
This program is used to find the most expensive moisterizer and add it to the cart
"""

from selenium import webdriver
import time

# Creating an instence of thw web browser and navigating to the Shopping page
browser = webdriver.Firefox()
browser.get('https://weathershopper.pythonanywhere.com/')

# Checking if the right web page has been loaded
if browser.title!="The best moisturizers in the world!":
    print("Error in loading page")
    browser.close()
    exit()
>>>>>>> 400f6bd19d9189db7bc0cd743bc3c4173eb2368f
