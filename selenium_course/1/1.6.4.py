import time
from selenium import webdriver

try:
    driver = webdriver.Chrome()
    driver.get('http://suninjuly.github.io/simple_form_find_task.html')
    field1 = driver.find_element_by_css_selector('.form-group:nth-child(1) input')
    field1.send_keys('Nikita')
    field2 = driver.find_element_by_css_selector('.form-group:nth-child(2) input')
    field2.send_keys('Efremov')
    field3 = driver.find_element_by_css_selector('.form-group:nth-child(3) input')
    field3.send_keys('N. Novgorod')
    field4 = driver.find_element_by_css_selector('.form-group:nth-child(4) input')
    field4.send_keys('Russian Federation')
    submit_button = driver.find_element_by_css_selector('#submit_button')
    submit_button.click()

finally:
    time.sleep(20)
    driver.quit()
    