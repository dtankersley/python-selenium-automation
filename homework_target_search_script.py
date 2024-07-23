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
driver.get('https://www.target.com/')

# wait for 8 sec
sleep(8)

#Click the sign-in button
#driver.find_element(By.XPATH, "//div[contains(@class, 'styles__LinkContainer')]/a[contains(@href, '/sign-in')]")
driver.find_element(By.XPATH, "//span[text()='Sign in']").click() # Click SignIn button
sleep(3)

#Click the Sign-in link from the side panel
#driver.find_element(By.XPATH, '//span["class="styles__ListItemText-sc-diphzn-1.jaMNVl"]').click()
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']//span[text()='Sign in']").click() #  Click SignIn button
sleep(3)

expected = 'Sign into your Target account'
actual = driver.find_element(By.XPATH, "//h1[contains(@class, 'StyledHeading')]").text
assert expected == actual, f'Expected {expected} did not match actual {actual}'
driver.find_element(By.ID, 'login')

driver.quit()