from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Open Dynamic Controls page
driver.get("https://the-internet.herokuapp.com/dynamic_controls")

# Click the Enable button
driver.find_element(By.XPATH, "//button[text()='Enable']").click()

# Create Explicit Wait
wait = WebDriverWait(driver, 10)

# Wait until the text box becomes clickable
textbox = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))
)

# Enter text
textbox.send_keys("Selenium Clickable Wait")

print("Textbox is enabled and text entered successfully.")

time.sleep(5)

driver.quit()