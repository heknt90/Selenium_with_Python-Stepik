import math
import time
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/find_xpath_form')

    inputs = browser.find_elements_by_xpath('//input[@type="text"]')
    
    for input in inputs:
        input.send_keys('text')   

    button = browser.find_element_by_xpath('//button[text()="Submit"]')

    button.click()

finally:
    time.sleep(10)
    browser.quit()
    