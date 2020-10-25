import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_check_trash(browser):
    browser.get(link)
    time.sleep(3)
    # s = "Ajouter au panier"
    # assert browser.find_element_by_css_selector('.btn-add-to-basket').text == s


