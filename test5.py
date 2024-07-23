from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Get automatically generated credit card details
    driver.get("https://demo.guru99.com/payment-gateway/cardnumber.php")
    time.sleep(3)

    # Wait for the card number to be present and receive it
    card_number_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#three > div > h4:nth-child(3)"))
    )
    full_card_number_data = card_number_element.text
    print(f"Full credit card number:{full_card_number_data}")
    card_number = ''.join(filter(str.isdigit, full_card_number_data))[-16:]
    print(f"Received Card Number: {card_number}")

    # Step 2: Go to the credit balance check page
    driver.get("https://demo.guru99.com/payment-gateway/check_credit_balance.php")
    # Step 3: Check the credit card balance
    card_input = driver.find_element(By.NAME, "card_nmuber")
    card_input.send_keys(card_number)
    time.sleep(3)
    # Click the check balance button
    check_balance_button = driver.find_element(By.NAME, "submit")
    check_balance_button.click()

    # Step 4: Confirm that no transfers have been done
    balance_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#three > div > font:nth-child(6)"))
    ).text

    print(f"Balance is:{balance_message}")
    assert "This Card Not Any Transactions" in balance_message
    print("Test case is successful")

finally:
    driver.quit()

