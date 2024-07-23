import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("https://demo.guru99.com/payment-gateway/purchasetoy.php")

    # Select 1 item from quantity dropdown
    quantity_dropdown = Select(driver.find_element(By.NAME, "quantity"))
    quantity_dropdown.select_by_value("1")
    time.sleep(3)

    # Click the "Buy Now" button
    buy_now_button = driver.find_element(By.XPATH, "//input[@value='Buy Now']")
    buy_now_button.click()
    time.sleep(3)

    # Wait for the payment page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "card_nmuber"))
    )

    # Enter VISA credit card details
    driver.find_element(By.NAME, "card_nmuber").send_keys("4111111111111111")

    expiration_month = Select(driver.find_element(By.NAME, "month"))
    expiration_month.select_by_value("12")

    expiration_year = Select(driver.find_element(By.NAME, "year"))
    expiration_year.select_by_value("2026")

    driver.find_element(By.NAME, "cvv_code").send_keys("123")
    time.sleep(3)

    # Click the "Pay" button
    pay_button = driver.find_element(By.NAME, "submit")
    pay_button.click()

    # Wait for and confirm successful payment
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Payment successfull!')]"))
    )

    assert "Payment successfull!" in success_message.text
    print("Payment successful!")

except Exception as e:
    print(f"Test failed: {str(e)}")

finally:
    # Close the browser
    driver.quit()

