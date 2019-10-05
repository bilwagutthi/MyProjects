"""
 Find the most expensive moisturizer and add it to the cart.

 SCOPE:
 1) Launch Firefox Driver
 2) Add all moisturizers to the cart
 3) Add that moisturizer to the cart
 4) Calculate number of products on the page
 5) Check if all the moisterizers are added by compareing the number of 
    products against the number of products in the cart
 6) Close the browser

Author : Bilwa Gutthi
"""

from selenium import webdriver
import time

# Creating an instence of thw web browser and navigating to the Shopping page
browser = webdriver.Firefox()
browser.get('https://weathershopper.pythonanywhere.com/moisturizer')

# Checking if the right web page has been loaded
if browser.title!="The best moisturizers in the world!":
    print("Error in loading page")
    browser.close()
    exit()
else:
    print("Page loaded")


# Finidng and clicking all add buttons
add_buttons=browser.find_elements_by_xpath('//button[contains(text(),"Add")]')
no_of_Products=len(add_buttons)
clicked_no=0
for i in add_buttons:
    i.click()
    clicked_no+=1
    print("No of add button clicked :",clicked_no)

print("Total no of products added : ",no_of_Products)

# Clicking on cart button to check if all moisterizer are added
cart_button=browser.find_element_by_xpath('//button[@class="thin-text nav-link"]')
cart_button.click()

# Checking total no of products in cart
products_added=browser.find_elements_by_xpath('//tbody/tr')
no_products_added=len(products_added)
print("No of products in cart : ",no_products_added)

if(no_of_Products==no_products_added):
    print("Success : All products added")
else:
    print("Fail : Unable to add all products")


browser.close()