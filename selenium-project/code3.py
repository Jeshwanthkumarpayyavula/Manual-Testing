from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/")
wait=WebDriverWait(driver,30)
login_page=wait.until(EC.visibility_of_element_located((By.ID,"1")))
# login_page=wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"jwCbxy")))
login_page.send_keys("7010794865")
continu=wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"FFO0ui")))
continu.click()
otp=wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"H6gpAI")))
time.sleep(20)
clic=wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"FFO0ui")))
clic.click()
tit=driver.title
exp="Online Shopping India Mobile, Cameras, Lifestyle & more Online @ Flipkart.com"
if tit==exp:
    print("Got it")
else:
    print("Something wrong")
time.sleep(20)
driver.quit()
