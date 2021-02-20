from selenium import webdriver
import time
import unittest


class TestUI(unittest.TestCase):
  
    def try_registration(self, url ):
        print(url)
        try: 
            browser = webdriver.Chrome()
            browser.get(url)

            for number in ('first', 'second', 'third'):
                selector = '.first_block .{}'.format(number)
                input = browser.find_element_by_css_selector(selector)
                input.send_keys('{} text'.format(number.capitalize()))

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(1)
            # закрываем браузер после всех манипуляций
            browser.quit()
    
    def test_first_page(self):
        url = "http://suninjuly.github.io/registration1.html"
        self.try_registration(url)

    def test_second_page(self):
        url = "http://suninjuly.github.io/registration2.html"
        self.try_registration( url)


if __name__ == '__main__':
    unittest.main()