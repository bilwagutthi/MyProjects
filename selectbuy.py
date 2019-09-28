"""
This program is used to find the value of temperature displayed and to click the appropriate button.
If temperature is less than 19 moisturizer button is selected.
If temperature is more than 34 sunscreen button is selected.
Once the button is selected the program checks wether the webbrowser is redirected to the appropriate page

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

#  Finding the tag with tempature value , finding the content of the tag and extracting the values
temperature_Box=browser.find_element_by_xpath('//span[@id="temperature"]').text.split(' ')

#Finding the temperature from the list of extracted values
temperature=int(temperature_Box[0])
print("The temperature is",temperature)

#If temperature is less than 19 Moisturizer button is clicked
if temperature<19:
    button_Moisturizer=browser.find_element_by_xpath('//a[@href="/moisturizer"]')
    button_Moisturizer.click()

#Cheacking if moisturizer button is clicked and if webbrowser is redirected to the correct page
    if browser.find_element_by_xpath('//h2["Moisturizers"]'):
        print("Temperature is less than 19 , hence moisturizers are selected")

#If temperature is more than 34 Sunscreen button is clicked
elif temperature>34:
    button_Sunscreen=browser.find_element_by_xpath('//a[@href="/sunscreen"]')
    button_Sunscreen.click()

#Cheacking if moisturizer button is clicked and if webbrowser is redirected to the correct page
    if browser.find_element_by_xpath('//h2["sunscreens"]'):
        print("Temperature is greater than 34 , hence sunscreens are selected")


time.sleep(3)
browser.close()
