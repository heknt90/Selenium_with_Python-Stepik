from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    # Открыть страницу http://SunInJuly.github.io/execute_script.html.
    browser.get('http://suninjuly.github.io/execute_script.html')

    # Считать значение для переменной x.
    x = int(browser.find_element_by_css_selector('#input_value').text)
    
    # Посчитать математическую функцию от x.
    result = calc(x)

    # Проскроллить страницу вниз.
    browser.execute_script('return window.scrollBy(0, 100)')

    # Ввести ответ в текстовое поле.
    input = browser.find_element_by_css_selector('#answer')
    input.send_keys(result)

    # Выбрать checkbox "I'm the robot".
    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    checkbox.click()

    # Переключить radiobutton "Robots rule!".
    radiobutton = browser.find_element_by_css_selector('#robotsRule')
    radiobutton.click()

    # Нажать на кнопку "Submit".
    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()

finally:
    time.sleep(10)
    browser.quit()