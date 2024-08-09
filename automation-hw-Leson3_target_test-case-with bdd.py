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

driver.get('https://www.target.com/')

# click the cart icon
driver.find_element(By.CSS_SELECTOR, '.sc-ab4ee1d1-1.sc-e9170b4b-0.bYXfno.jMCzsf').click()

# wait for the page with search results to load
sleep(6)

# verify
expected_text = 'Your cart is empty'
actual_text = driver.find_element(By.CSS_SELECTOR, ".sc-fe064f5c-0.dtCtuk").text
# print(actual_text)
assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'

print('Test case passed')
driver.quit()