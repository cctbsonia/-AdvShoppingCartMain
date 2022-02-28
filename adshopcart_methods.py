import sys
import datetime
import adshopcart_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome('/Users/soniamacbookair/PycharmProjects/python_cctb/chromedriver')

# Fixture method - to open web browser
def setUp():
    # Make a full screen
    driver.maximize_window()

    # Let's wait for the browser response in general
    driver.implicitly_wait(30)

    # Navigating to the Advantage Shopping website
    driver.get(locators.adshop_url)


    # Print test start day and time
    if driver.current_url == locators.adshop_url:
        print(f'Test start at: {datetime.datetime.now()}')

    # Checking we are on the correct URL address and we are seeing correct title
    if driver.current_url == locators.adshop_url and driver.title == ' Advantage Shopping':
        print(f'We are at Advantage Shopping homepage -- {driver.current_url}')
        print(f'We\'re seeing title message -- {driver.title}')
    else:
        print(f'We\'re not at the Advantage Shopping homepage. Check your code!')
        driver.close()
        driver.quit()

# Fixture method - to close web browser
def tearDown():
    if driver is not None:
        print(f'------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()


setUp()
tearDown()
