from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    # Открыть страницу http://suninjuly.github.io/selects1.html
    browser.get('http://suninjuly.github.io/selects1.html')

    num1 = int(browser.find_element_by_css_selector('#num1').text)
    num2 = int(browser.find_element_by_css_selector('#num2').text)
    
    # Посчитать сумму заданных чисел
    sum = str(num1 + num2)

    print(sum)

    # Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element_by_css_selector('#dropdown'))
    select.select_by_value(sum)

    # Нажать на кнопку "Submit".
    submit_button = browser.find_element_by_css_selector('button[type="submit"]')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()