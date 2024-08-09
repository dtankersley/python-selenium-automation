from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ref=ap_frn_logo')

#Amazon logo
driver.find_element(By.CSS_SELECTOR, '[aria-label="Amazon"]')

#Creat Account text
driver.find_element(By.CSS_SELECTOR, '.a-spacing-small')


# select sign-in link
driver.find_element(By.CSS_SELECTOR, "'#nav-link-accountList-nav-line-1").click()

# Select to create a new account
driver.find_element(By.CSS_SELECTOR, '#createAccountSubmit').click()


# customer name field
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name") # by 'ID'
driver.find_element(By.CSS_SELECTOR, ".a-span12.auth-autofocus.auth-required-field") # By Class
driver.find_element(By.CSS_SELECTOR, "[placeholder='First and last name']")  # By Attribute

# mobile number / email field
driver.find_element(By.CSS_SELECTOR, '#ap_email')  #By ID
driver.find_element(By.CSS_SELECTOR, ".a-input-text.a-span12.a-spacing-micro.auth-required-field.auth-require-claim-validation") # by class)
driver.find_element(By.CSS_SELECTOR, "[type='email']")   #search by attribute

# password field
driver.find_element(By.CSS_SELECTOR, '#ap_password')  # search by id
driver.find_element(By.CSS_SELECTOR, "a-input-text.auth-required-field.auth-require-fields-match auth-require-password-validation")  # by Class
driver.find_element(By.CSS_SELECTOR, "[name='passwordCheck']")  # by attribute

# Re-enter password
driver.find_element(By.CSS_SELECTOR, '#ap_password_check') # By ID
driver.find_element(By.CSS_SELECTOR, '.auth-require-fields-match')  # by class
driver.find_element(By.CSS_SELECTOR, "[name='passwordCheck']")  # by attribute


# Continue button
driver.find_element(By.CSS_SELECTOR, 'continue') # by ID
driver.find_element(By.CSS_SELECTOR, "[type='submit']")   # by attribute
driver.find_element(By.CSS_SELECTOR, '.a-button-input')  #class

# Conditions of use
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")

# Privacy Notice
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")

#sign-in link
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")