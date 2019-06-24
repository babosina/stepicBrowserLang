import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_presents_on_the_page(browser):
    browser.get(link)
    browser.find_element_by_id("add_to_basket_form")
    time.sleep(5)  # in case you want to check 'fr'
