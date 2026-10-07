from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Open Dynamic Loading page
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

# Click Start button
driver.find_element(By.XPATH, "//button[text()='Start']").click()

# Create Explicit Wait
wait = WebDriverWait(driver, 10)

# Wait until "Hello World!" is visible
hello_text = wait.until(
    EC.visibility_of_element_located((By.ID, "finish"))
)

# Print the result
print("Message:", hello_text.text)

time.sleep(5)
driver.quit()