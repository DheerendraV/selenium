from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
ser = webdriver.ChromeService(executable_path="/Users/dheerendravarmapenmatsa/drivers/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=ser,options=option)
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(1)
driver.find_element(By.XPATH,"//*[text()='Create new account']").click()
time.sleep(2)
driver.find_element(By.NAME,"firstname").send_keys("Dheerendra Varma")
driver.find_element(By.NAME,"lastname").send_keys("Penmatsa")
driver.find_element(By.NAME,"reg_email__").send_keys("9512137899")
driver.find_element(By.NAME,"reg_passwd__").send_keys("Dheeru@2107")
sel1=Select(driver.find_element(By.XPATH,"//select[@id='month']"))
sel1.select_by_visible_text("Jul")
sel2=Select(driver.find_element(By.XPATH,"//*[@id='day']"))
sel2.select_by_visible_text("21")
sel3=Select(driver.find_element(By.XPATH,"//*[@id='year']"))
sel3.select_by_visible_text("2000")
driver.find_element(By.XPATH,"//*[text()='Male']").click()
driver.find_element(By.XPATH,"//button[text()='Sign Up']").click()
time.sleep(20)
element = driver.find_elements(By.XPATH,"//*[text()='Dheerendra Varma' or text()='Update contact info']")
print(len(element))
if len(element)>0:
    print("Registration Test case Passed")
else:
    print("Registration Test case Failed")