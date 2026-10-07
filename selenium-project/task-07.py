from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/web/alerts.html")

wait = WebDriverWait(driver, 10)

# ------------------------------------------------
# 1. Simple Alert
# ------------------------------------------------

driver.find_element(By.ID, "alert").click()

alert = wait.until(EC.alert_is_present())

print("Simple Alert:")
print(alert.text)
time.sleep(5)

alert.accept()


# ------------------------------------------------
# 2. Confirmation Alert - Accept
# ------------------------------------------------

driver.find_element(By.ID, "confirm").click()

alert = wait.until(EC.alert_is_present())

print("\nConfirmation Alert:")
print(alert.text)
time.sleep(5)

alert.accept()


# ------------------------------------------------
# 3. Confirmation Alert - Dismiss
# ------------------------------------------------

driver.find_element(By.ID, "confirm").click()

alert = wait.until(EC.alert_is_present())

print("\nConfirmation Alert:")
print(alert.text)

alert.dismiss()


# ------------------------------------------------
# 4. Prompt Alert
# ------------------------------------------------

driver.find_element(By.ID, "prompt").click()

alert = wait.until(EC.alert_is_present())

print("\nPrompt Alert:")
print(alert.text)

alert.send_keys("Python")

alert.accept()


# ------------------------------------------------
# Close Browser
# ------------------------------------------------

driver.quit()




# Drop Down
country = Select(driver.find_element(By.ID, "country"))
country.select_by_visible_text("India")
country.select_by_value("IN")
country.select_by_index(2)
for option in country.options:
    print(option.text)