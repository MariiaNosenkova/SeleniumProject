from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    driver.get("https://demo.guru99.com/payment-gateway/cardnumber.php")
    card_number_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#three > div > h4:nth-child(3)"))
    )
    full_card_number_data = card_number_element.text
    card_number = ''.join(filter(str.isdigit, full_card_number_data))[-16:]


    cvv_card_data_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#three > div > h4:nth-child(4)"))
    )
    full_cvv_card_data = cvv_card_data_element.text
    print(f"full_cvv_card_data: {full_cvv_card_data}")
    cvv_number = ''.join(filter(str.isdigit, full_cvv_card_data))


    month_year_card_data_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#three > div > h4:nth-child(5)"))
    )
    full_year_month_card_data = month_year_card_data_element.text
    month_number = ''.join(filter(str.isdigit, full_year_month_card_data))[0:2]
    year_number = ''.join(filter(str.isdigit, full_year_month_card_data))[-4:]


    print(f"Received Card Number: {card_number}")
    print(f"Received CVV: {cvv_number}")
    print(f"Received year: {year_number}")
    print(f"Received month: {month_number}")

#Purchase toy
    driver.get("https://demo.guru99.com/payment-gateway/purchasetoy.php")
    quantity_select = Select(driver.find_element(By.NAME, "quantity"))
    quantity_select.select_by_value("2")
    buy_now_button = driver.find_element(By.XPATH, "//input[@value='Buy Now']")
    time.sleep(2)
    buy_now_button.click()
    time.sleep(4)

#Proccess payment
    driver.get("https://demo.guru99.com/payment-gateway/process_purchasetoy.php")
#Enter card details
    enter_card_number = driver.find_element(By.CSS_SELECTOR, "#card_nmuber")
    enter_card_number.send_keys(card_number)
    enter_cvv_card_number = driver.find_element(By.ID, "cvv_code").send_keys(cvv_number)
    enter_month_card = driver.find_element(By.ID, "month").send_keys(month_number)
    enter_year_card = driver.find_element(By.ID, "year").send_keys(year_number)
#Click button
    pay_now_button = driver.find_element(By.NAME, "submit")
    #pay_now_button.click()
    time.sleep(5)

#Check card balance
    driver.get("https://demo.guru99.com/payment-gateway/check_credit_balance.php")
    card_input = driver.find_element(By.NAME, "card_nmuber")
    card_input.send_keys(card_number)
    time.sleep(3)
    # Click the check balance button
    check_balance_button = driver.find_element(By.NAME, "submit")
    check_balance_button.click()
    time.sleep(2)
   # Step 4: Confirm that no transfers have been done
    balance_message = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.CSS_SELECTOR, "#three > div > font:nth-child(6)"))
    ).text
    print(balance_message)
   #assert "No transfers have been done" in balance_message


finally:
    driver.quit()

