from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get('http://google.com')

x = browser.find_element_by_css_selector('.gLFyf')
x.send_keys('pasaporte biometrico ecuador')
x.submit()

time.sleep(1)

y = browser.find_element_by_link_text('Noticias')
y.click()

time.sleep(1)

