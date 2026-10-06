from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com/")

search = driver.find_element(By.NAME, "q")

search.send_keys("Actor Ramcharan")

print(search.get_attribute("value"))

search.send_keys(Keys.ENTER)

time.sleep(3)

driver.get("https://en.wikipedia.org/wiki/Ram_Charan")

time.sleep(10)