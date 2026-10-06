from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time


driver = webdriver.Chrome()
driver.maximize_window()


def fill_text(name, value):
    for attempt in range(5):
        try:
            element = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, name))
            )
            driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});",
                element,
            )
            element.clear()
            element.send_keys(value)
            time.sleep(0.2)
            if element.get_attribute("value") == value:
                return
            driver.execute_script(
                "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('input', {bubbles: true}));",
                element,
                value,
            )
            if element.get_attribute("value") == value:
                return
        except StaleElementReferenceException:
            continue
    raise RuntimeError(f"Could not fill field: {name}")


def click_by_id(element_id):
    for attempt in range(5):
        try:
            element = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, element_id))
            )
            driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'instant', block: 'center'}); arguments[0].click();",
                element,
            )
            return
        except StaleElementReferenceException:
            continue
    raise RuntimeError(f"Could not click element: {element_id}")


def ensure_value(name, expected_value):
    for _ in range(5):
        try:
            element = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, name))
            )
            current_value = element.get_attribute("value")
            if current_value == expected_value:
                return True
            driver.execute_script(
                "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('input', {bubbles: true}));",
                element,
                expected_value,
            )
            if element.get_attribute("value") == expected_value:
                return True
        except StaleElementReferenceException:
            continue
    return False


driver.get("https://vinothqaacademy.com/demo-site/")
wait = WebDriverWait(driver, 20)

# Fill required personal details
fill_text("vfb-5", "Jeshwanth")
print("First Name value:", driver.find_element(By.NAME, "vfb-5").get_attribute("value"))
fill_text("vfb-7", "Kumar")
print("Last Name value:", driver.find_element(By.NAME, "vfb-7").get_attribute("value"))
click_by_id("vfb-31-1")  # Male
print("Gender selected:", driver.find_element(By.ID, "vfb-31-1").is_selected())
click_by_id("vfb-20-0")  # Selenium WebDriver
click_by_id("vfb-20-1")  # Java

# Fill address details
fill_text("vfb-13[address]", "123 ABC Street")
fill_text("vfb-13[address-2]", "Apartment 12")
fill_text("vfb-13[city]", "Chennai")
fill_text("vfb-13[state]", "Tamil Nadu")
fill_text("vfb-13[zip]", "600001")
country = Select(driver.find_element(By.NAME, "vfb-13[country]"))
country.select_by_visible_text("India")

# Fill contact and query details
fill_text("vfb-14", "jeshwanthkumarpayyavula@gmail.com")
fill_text("vfb-18", "12/25/2026")
Select(driver.find_element(By.NAME, "vfb-16[hour]")).select_by_value("10")
Select(driver.find_element(By.NAME, "vfb-16[min]")).select_by_value("30")
fill_text("vfb-19", "9121913227")
fill_text("vfb-23", "I want to learn Selenium Automation.")

# Verification code shown on the page
fill_text("vfb-3", "33")

# Final safety check before submission
if not ensure_value("vfb-5", "Jeshwanth"):
    raise RuntimeError("First Name is empty before submit.")
if not ensure_value("vfb-7", "Kumar"):
    raise RuntimeError("Last Name is empty before submit.")
if not driver.find_element(By.ID, "vfb-31-1").is_selected():
    click_by_id("vfb-31-1")

# Click submit
submit_btn = wait.until(EC.element_to_be_clickable((By.ID, "vfb-4")))
submit_btn.click()

print("Form submitted successfully!")

time.sleep(20)
driver.quit()