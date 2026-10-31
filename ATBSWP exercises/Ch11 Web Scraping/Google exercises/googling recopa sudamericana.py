from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://google.com')
x = browser.find_element_by_css_selector('.gLFyf')
x.send_keys('recopa sudamericana')
x.submit()
