from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    
    # Открыть страницу http://suninjuly.github.io/redirect_accept.html
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    # Нажать на кнопку
    magical_button = browser.find_element_by_css_selector('button[type="submit"]')
    magical_button.click()

    # Переключиться на новую вкладку
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    # Пройти капчу для робота и получить число-ответ
    x = browser.find_element_by_css_selector('#input_value').text
    y = calc(x)
    input = browser.find_element_by_css_selector('#answer')
    input.send_keys(y)

    button2 = browser.find_element_by_css_selector('button[type="submit"]')
    button2.click()

finally:
    time.sleep(10)
    browser.quit()