import time

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'

def test_check_presence_button_basket(browser):
    browser.get(link)
    time.sleep(30)
    button_basket = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary")
    assert button_basket, 'There is no button basket.'