#Find the Amazon Logo
driver.findelement(By.XPATH, '//i[@aria-label="Amazon"}')


#Find the Email field
driver.findelement(By.XPATH, '//input[@type="email"]')


#Continue Button
driver.find_element(By.ID, 'continue')
driver.findelement(By.XPATH, '//input[@type="submit"]')

#Conditions of use link
driver.findelement(By.ID,"legalTextRow")
driver.findelement(By.XPATH, '//div[@class="a-row a-spacing-top-medium a-size-small"]')

#Privacy Notice Link"
driver.find_element(By.ID, "a-page")

#Need Help Link
driver.find_element(By.XPATH,'//span[@class="a-expander-prompt"]')

#Forgot Password
driver.find_element(By.ID, "auth-fpp-link-bottom")
driver.find_element(By.XPATH, '//a[@class="a-link-normal"]')

#Other issues with Sign in
driver.find_element(By.ID, "ap-other-signin-issues-link")

#Create your Amazon Account
driver.find_element(By.ID, "createAccountSubmit")