# Полезные методы библиотеки Selenium

    from selenium import webdriver

    webdriver.Chrome()
    browser = webdriver.Chrome()

    browser.get(url)
    browser.find_element_by_css_selector(selector)
    element.send_keys('Nikita')
    element.click()
    element.get_attribute(attr_name)
    element.text

## Работа с выпадающим списком

    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_css_selector(select_selector))
    select.select_by_value(needed_value)

    browser.execute_script('return window.scrollBy(0, 100)')

### Принять confirm

    confirm = browser.switch_to.alert
    confirm.accept()

### Переключиться на новую вкладку

    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

### Wait

    browser.implicitly_wait(5)

or

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    # Ожидание в течении 12 секунд, пока элемент с id element_id не будет содержать текст text_content
    element = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, element_id), text_content)
    )

## Устанавливаем размер окна

    driver.set_window_position(0, 0)
    driver.set_window_size(360, 568)

## Скриншот страницы

    browser.save_screenshot('sr.png')

## Завершить тест

    browser.quit()
