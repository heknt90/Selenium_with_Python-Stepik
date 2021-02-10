from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/math.html')
    # Считать значение для переменной x.
    x = browser.find_element_by_css_selector('#input_value').text
    # Посчитать математическую функцию от x (код для этого приведён ниже). ln(abs(12*sin(x)))
    answer = calc(x)
    # Ввести ответ в текстовое поле.
    answer_input = browser.find_element_by_css_selector('#answer')
    answer_input.send_keys(answer)
    # Отметить checkbox "I'm the robot".
    robot_checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    robot_checkbox.click()
    # Выбрать radiobutton "Robots rule!".
    radio_button = browser.find_element_by_css_selector('#robotsRule')
    radio_button.click()
    # Нажать на кнопку Submit.
    submit_button = browser.find_element_by_css_selector('button[type="submit"]')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()