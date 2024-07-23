from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Step 1: Go to the purchase page
driver.get("https://demo.guru99.com/payment-gateway/purchasetoy.php")

# Step 2: Choose 2 items
quantity_select = Select(driver.find_element(By.NAME, "quantity"))
quantity_select.select_by_value("2")
time.sleep(4)

# Step 3: Click the "Buy Now" button
buy_now_button = driver.find_element(By.XPATH, "//input[@value='Buy Now']")
buy_now_button.click()
time.sleep(3)

# Wait for the next page to load
WebDriverWait(driver, 10).until(EC.url_to_be("https://demo.guru99.com/payment-gateway/process_purchasetoy.php"))

# Step 4: Check if the amount equals $40
amount_element = driver.find_element(By.CSS_SELECTOR,".row font:nth-child(2)")

amount = amount_element.text
assert amount == "$40.00", f"Expected amount to be $40, but got {amount}"
print("amount:" + amount)
print("The test case is successful")

driver.quit()
