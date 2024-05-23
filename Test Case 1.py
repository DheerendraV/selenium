import os

from selenium import webdriver
from selenium.webdriver.common.by import By

cService = webdriver.ChromeService(executable_path='/Users/dheerendravarmapenmatsa/drivers/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service = cService)
driver.get('https://www.facebook.com/login/')

driver.find_element(By.ID,"email").send_keys("Admin@gmail.com")
driver.find_element(By.ID,"pass").send_keys("admin@1234")
driver.find_element(By.ID,"loginbutton").click()
actual_title = driver.title
expected_title = "OrangeHRM"
if actual_title == expected_title:
    print("login test case passed")
else:
    print("login test case failed")


