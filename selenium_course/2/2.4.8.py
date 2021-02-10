from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)

    # Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)


    button = browser.find_element_by_id("book")
    price_element = browser.find_element_by_id('price')
    
    price_span = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'),'$100')
    )
    
    # Нажать на кнопку "Book"
    button.click()

    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

    x = browser.find_element_by_css_selector('#input_value').text
    y = calc(x)
    input = browser.find_element_by_css_selector('#answer')
    input.send_keys(y)

    submit_button = browser.find_element_by_css_selector('button[type="submit"]')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()