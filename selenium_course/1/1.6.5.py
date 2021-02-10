import math
import time
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/find_link_text')
    link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()

    f1 = browser.find_element_by_css_selector('.form-group:nth-child(1) input')
    f2 = browser.find_element_by_css_selector('.form-group:nth-child(2) input')
    f3 = browser.find_element_by_css_selector('.form-group:nth-child(3) input')
    f4 = browser.find_element_by_css_selector('.form-group:nth-child(4) input')

    f1.send_keys('alala')
    f2.send_keys('alala')
    f3.send_keys('alala')
    f4.send_keys('alala')

    button = browser.find_element_by_css_selector('button[type="submit"]')

    button.click()

finally:
    time.sleep(40)
    browser.quit()
    