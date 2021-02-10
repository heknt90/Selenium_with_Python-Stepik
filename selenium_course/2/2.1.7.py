from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    # Открыть страницу http://suninjuly.github.io/get_attribute.html.
    browser.get('http://suninjuly.github.io/get_attribute.html')
    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    img = browser.find_element_by_css_selector('[valuex]')
    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    x = img.get_attribute('valuex')
    # Посчитать математическую функцию от x (сама функция остаётся неизменной).
    result = calc(x)
    # Ввести ответ в текстовое поле.
    text_input = browser.find_element_by_css_selector('#answer')
    text_input.send_keys(result)
    # Отметить checkbox "I'm the robot".
    robots_checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    robots_checkbox.click()
    # Выбрать radiobutton "Robots rule!".
    radio_button = browser.find_element_by_css_selector('#robotsRule')
    radio_button.click()
    # Нажать на кнопку "Submit".

    submit_button = browser.find_element_by_css_selector('button[type="submit"]')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()