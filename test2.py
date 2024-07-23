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

# Step 2: Choose 4 items
quantity_select = Select(driver.find_element(By.NAME, "quantity"))
quantity_select.select_by_value("4")
time.sleep(4)

# Step 3: Press the "Buy Now" button
buy_now_button = driver.find_element(By.XPATH, "//input[@value='Buy Now']")
buy_now_button.click()
time.sleep(3)

# Wait for the next page to load
WebDriverWait(driver, 10).until(EC.url_to_be("https://demo.guru99.com/payment-gateway/process_purchasetoy.php"))

# Step 5: Check if the amount equals $80
amount_element = driver.find_element(By.CSS_SELECTOR,".row font:nth-child(2)")
amount = amount_element.text

assert amount == "$80.00", f"Expected amount to be $80, but got {amount}"
# print("Test passed: Amount is $80 for 4 items")
print("amount:" + amount)
print("Test is successful")

# Step 6: Close the browser
driver.quit()
