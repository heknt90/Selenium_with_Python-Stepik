from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    
    # Открыть страницу http://suninjuly.github.io/file_input.html
    browser.get('http://suninjuly.github.io/file_input.html')

    # Заполнить текстовые поля: имя, фамилия, email
    first_name_input = browser.find_element_by_css_selector('input[name="firstname"]')
    first_name_input.send_keys('Vasya')
    last_name_input = browser.find_element_by_css_selector('input[name="lastname"]')
    last_name_input.send_keys('Pupkin')
    email_input = browser.find_element_by_css_selector('input[name="email"]')
    email_input.send_keys('example.com')

    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    file_input = browser.find_element_by_css_selector('#file')
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'file.example.txt')
    file_input.send_keys(file_path)
    
    # Нажать кнопку "Submit"
    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()

finally:
    time.sleep(10)
    browser.quit()