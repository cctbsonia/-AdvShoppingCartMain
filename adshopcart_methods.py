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

def signUp():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(3)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(3)
    driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.new_username)
    sleep(0.25)
    driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
    sleep(0.25)
    driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.NAME,'confirm_passwordRegisterPage').send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.NAME,'first_nameRegisterPage').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.NAME,'phone_numberRegisterPage').send_keys(locators.phone)
    sleep(0.25)
    Select(driver.find_element(By.NAME,'countryListboxRegisterPage')).select_by_visible_text('Canada')
    sleep(0.25)
    driver.find_element(By.NAME,'cityRegisterPage').send_keys(locators.city)
    sleep(0.25)
    driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
    sleep(0.25)
    driver.find_element(By.NAME,'state_/_province_/_regionRegisterPage').send_keys(locators.province)
    sleep(0.25)
    driver.find_element(By.NAME,'postal_codeRegisterPage').send_keys(locators.postal_code)
    sleep(0.25)
    driver.find_element(By.NAME,'allowOffersPromotion').click()
    sleep(0.25)
    driver.find_element(By.NAME,'i_agree').click()
    sleep(0.25)
    driver.find_element(By.ID,'register_btnundefined').click()
    sleep(3)
    driver.find_element(By.ID, 'menuUser').click()
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[1]').click()
    sleep(2)


def check_my_account_display_full_name():
    if driver.current_url == locators.my_account_url:
        if driver.find_element(By.XPATH, f'//label[contains(.,"{locators.full_name}")]').is_displayed():
            print(f'------------------------------------')
            print(f'User with the name {locators.full_name} is displayed. Create account passed.')
        else:
            print('User name not displayed. Check your code.')


def check_no_order():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[2]').click()
    sleep(2)
    if driver.find_element(By.XPATH, f'//label[contains(.," - No orders - ")]').is_displayed():
        print(f'------------------------------------')
        print(f'Confirmed No order is displayed')


def sign_out():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
    sleep(3)

def log_in():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(3)
    driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
    sleep(2)
    driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
    sleep(2)
    driver.find_element(By.ID,'sign_in_btnundefined').click()
    sleep(2)


def delete_account():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[1]').click()
    sleep(2)
    driver.execute_script("window.scrollTo(1000,1000 )")
    driver.find_element(By.XPATH, '//*[@id="myAccountContainer"]/div[6]/button/div').click()
    sleep(5)
    driver.find_element(By.XPATH, '//div[text()="yes"]').click()
    sleep(5)


def check_re_login():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(3)
    driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
    sleep(2)
    driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
    sleep(2)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(5)
    if driver.find_element(By.ID,'signInResultMessage'):
        print(f'------------------------------------')
        print(f'Re-login failed. Test passed. ')
    else:
        print('Check your code for error.')


# setUp()
# signUp()
# check_my_account_display_full_name()
# check_no_order()
# sign_out()
# log_in()
# delete_account()
# check_re_login()
# tearDown()

