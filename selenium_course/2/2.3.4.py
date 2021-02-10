from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    
    # Открыть страницу http://suninjuly.github.io/alert_accept.html
    browser.get('http://suninjuly.github.io/alert_accept.html')

    # Нажать на кнопку
    button1 = browser.find_element_by_css_selector('button[type="submit"]')
    button1.click()

    # Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    x = browser.find_element_by_css_selector('#input_value').text
    y = calc(x)
    input = browser.find_element_by_css_selector('#answer')
    input.send_keys(y)
    
    # Нажать кнопку "Submit"
    button2 = browser.find_element_by_css_selector('button[type="submit"]')
    button2.click()

finally:
    time.sleep(10)
    browser.quit()