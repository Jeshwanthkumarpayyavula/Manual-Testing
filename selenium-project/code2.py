from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

wait = WebDriverWait(driver, 10)

wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
)

product_name = input("Enter product name: ")

products = driver.find_elements(By.CLASS_NAME, "inventory_item")

found = False

for product in products:

    name = product.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text

    if name.lower() == product_name.lower():

        button = product.find_element(
            By.TAG_NAME,
            "button"
        )

        button.click()

        print(product_name, "added to cart")

        found = True
        break


if not found:
    print("Product not found")

time.sleep(2)

driver.find_element(
    By.CLASS_NAME,
    "shopping_cart_link"
).click()

time.sleep(5)

driver.quit()