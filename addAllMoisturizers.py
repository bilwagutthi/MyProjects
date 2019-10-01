"""
Find the most expensive moisturizer and add it to the cart.

SCOPE:
1) Launch Firefox Driver
2) Add all moisturizers to the cart
3) Add that moisturizer to the cart
4) Calculate sum of products
5) Check if all the moisterizers are added by compareing the sum against the total of the cart
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

# Creating a list with prizes of all moistirizers and finding the total
sum_products=0
prices=browser.find_elements_by_xpath('//div[@class="text-center col-4"]//descendant::p[contains(text(),"Price")]')
for i in prices:
    price=int(i.text.strip("Price: Rs. "))
    sum_products=sum_products+price

print("Sum is ",sum_products)
# Clicking all add buttons
add_buttons=browser.find_elements_by_xpath('//button[contains(text(),"Add")]')
j=0
for i in add_buttons:
    i.click()
    j+=1
    print("Added",j)

# Clicking on cart button to check if all moisterizer are added
cart_button=browser.find_element_by_xpath('//button[@class="thin-text nav-link"]')
cart_button.click()

# Checking total against sum
total_price=browser.find_element_by_xpath('//p[@id="total"]').text
total_price=int(total_price.strip("Total: Rupees "))
print("Total price in cart",total_price)
if sum_products==total_price:
    print("Successfully added all the moisterizers")
else:
    print("Fail")


time.sleep(3)

browser.close()