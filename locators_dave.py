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
driver.get('https://www.amazon.com/')

# Search by ID
driver.find_element(By.ID, 'nav-search-submit-button')
driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.ID, 'glow-ingress-line2')
#driver.find_element(By.ID, 'CardInstanceGMMrqMY7AQVB5CKrBSc0Kw'))

#Search by XPath
driver.find_element(By.XPATH, "//input@aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//input{@name='field-keywords']")

# by XPath with multiple attributes
driver.find_element(By.XPATH, "//input(@class='nav-input nav-progressive-attribute' and @value='Go']")
driver.find_element(By.XPath, "//input[@value='Go' and @class='nave-input nave-progressive-attribute' and @type='submiy']")

#Search by XPath with text()
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//a[text()-'Best Sellers' and @class='nav-a ']")

# contains()
driver.find_element(By.XPATH, "//h2[contains(text(), 'Scary good')]")
driver.find_element(By.XPATH, "//input[contains(aria-label, 'search ')]")

#From parent to child
driver.find_element(By.XPATH, "//div[@is='nav-main']//a{text()='Best Sellers']")



