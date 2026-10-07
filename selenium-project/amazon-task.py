import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME_USER_DATA_DIR = os.getenv(
    "CHROME_USER_DATA_DIR",
    r"C:\Users\admin\AppData\Local\Google\Chrome\User Data",
)
CHROME_PROFILE = os.getenv("CHROME_PROFILE", "Default")
AMAZON_EMAIL = os.getenv("AMAZON_EMAIL")
AMAZON_PASSWORD = os.getenv("AMAZON_PASSWORD")
product_url = "https://www.amazon.in/dp/B0BY8RXZ32"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument(f"--user-data-dir={CHROME_USER_DATA_DIR}")
options.add_argument(f"--profile-directory={CHROME_PROFILE}")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)


def page_has_amazon_challenge(driver):
    page = driver.page_source.lower()
    return (
        "verify you're not a robot" in page
        or "challenge-container" in page
        or "awswaf" in page
        or "captcha" in page
    )


def login_to_amazon_if_needed(driver, wait):
    # If the profile is already signed in, Amazon will simply open the product page without login.
    # If the profile is not logged in, this fallback tries the normal login flow.
    driver.get("https://www.amazon.in/")
    if "nav-link-accountList" in driver.page_source:
        return

    if not AMAZON_EMAIL or not AMAZON_PASSWORD:
        raise RuntimeError(
            "Chrome profile is not signed into Amazon and no AMAZON_EMAIL/AMAZON_PASSWORD were set. "
            "Either sign in manually in the browser profile or set the environment variables."
        )

    driver.get("https://www.amazon.in/ap/signin")
    if page_has_amazon_challenge(driver):
        input(
            "Amazon is showing a verification challenge. Solve it in the browser and press Enter to continue: "
        )

    email_field = wait.until(EC.visibility_of_element_located((By.ID, "ap_email")))
    email_field.clear()
    email_field.send_keys(AMAZON_EMAIL)
    driver.find_element(By.ID, "continue").click()

    password_field = wait.until(EC.visibility_of_element_located((By.ID, "ap_password")))
    password_field.clear()
    password_field.send_keys(AMAZON_PASSWORD)
    driver.find_element(By.ID, "signInSubmit").click()

    try:
        otp_input = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//input[contains(@name, 'otp') or contains(@id, 'otp') or contains(@name, 'code') or contains(@id, 'code')][not(@type='hidden')]",
                )
            )
        )
        otp = input("Enter the OTP sent to your phone and press Enter: ")
        otp_input.clear()
        otp_input.send_keys(otp)

        verify_button = driver.find_element(
            By.XPATH,
            "//input[contains(@name, 'verify') or contains(@id, 'verify') or contains(@name, 'continue') or contains(@id, 'continue') or @type='submit']",
        )
        verify_button.click()
    except Exception:
        pass


# Create a browser instance and open the product page directly.
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)

login_to_amazon_if_needed(driver, wait)
driver.get(product_url)
wait.until(EC.title_contains("Samsung Galaxy S23"))

# Amazon often renders a hidden duplicate Add to Cart button before the visible one; select the visible element.
wait.until(lambda d: any(btn.is_displayed() for btn in d.find_elements(By.ID, "add-to-cart-button")))
add_to_cart = next(
    btn for btn in driver.find_elements(By.ID, "add-to-cart-button") if btn.is_displayed()
)
add_to_cart.click()
time.sleep(20)

print("Product added to cart successfully!")

driver.quit()