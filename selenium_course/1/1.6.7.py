import math
import time
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/huge_form.html')

    inputs = browser.find_elements_by_css_selector('input[type="text"]')

    for input in inputs:
        input.send_keys('text')   

    button = browser.find_element_by_css_selector('button[type="submit"]')

    button.click()

finally:
    time.sleep(10)
    browser.quit()
    