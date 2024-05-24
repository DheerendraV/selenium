import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
cService = webdriver.ChromeService(executable_path='/Users/dheerendravarmapenmatsa/drivers/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service = cService)
driver.get('https://opensource-demo.orangehrmlive.com/')
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
time.sleep(1)
actual_title = driver.title
expected_title = "OrangeHRM"
if actual_title == expected_title:
    print("login test case passed")
else:
    print("login test case failed")


