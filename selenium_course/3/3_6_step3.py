from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math
import pytest

lessons = (236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905)

@pytest.fixture
def answer():
    return str(math.log(int(time.time() + 35)))

@pytest.fixture
def browser():
    print("\nstart browser for tet...")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser...")
    browser.quit()

class Test_Solutions:

    @pytest.mark.parametrize('lesson', lessons)
    def test_is_solution_correct(self, browser, answer, lesson):
        # открыть страницу 
        link = f"https://stepik.org/lesson/{lesson}/step/1"
        browser.get(link)

        # time.sleep(10)

        # ввести правильный ответ 
        input = browser.find_element_by_css_selector('.textarea.string-quiz__textarea')
        input.send_keys(answer)

        # нажать кнопку "Отправить" 
        submit = browser.find_element_by_css_selector('.submit-submission')
        submit.click()

        # дождаться фидбека о том, что ответ правильный 
        feedback = WebDriverWait(browser, 9).until(
            EC.presence_of_element_located((By.CSS_SELECTOR , '.attempt-wrapper.correct'))
        )

        # проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
        check_text = feedback.find_element_by_css_selector('.smart-hints__hint')
        assert check_text.text == 'Correct!', f"unexpected response {check_text.text}"
