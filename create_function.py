def correct_name(func, *args):
    func = func.__name__.replace('_', ' ').capitalize()
    print(func, *args)


def open_browser(browser_name):
    correct_name(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    correct_name(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    correct_name(find_registration_button_on_login_page, page_url, button_text)


open_browser(browser_name = 'Chrome')
go_to_companyname_homepage(page_url = 'https://google.com')
find_registration_button_on_login_page(page_url = 'https://google.com', button_text = 'Login')