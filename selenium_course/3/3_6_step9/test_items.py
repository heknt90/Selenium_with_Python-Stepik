# Run with
# pytest --browser_name=firefox --language=ru .\test_items.py

import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_see_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(5)
    button = None
    try:
        button = browser.find_element_by_css_selector('.btn-add-to-basket')
    except:
        pass
    assert button is not None, "Кнопка добавления в корзину не найдена на странице!"