 I have prepared three test scenarios for the training website: https://demo.guru99.com/payment-gateway/purchasetoy.php 
Each scenario includes two test cases. The details of the test scenarios and test cases, along with their steps, are outlined below. I identified the following key areas for testing: 
1.	Quantity Payment Verification 
Purchase 2 and 4 items and confirm that the total payment amount updates accordingly

2.	Card Type Payment Verification
Test payments using two different types of cards (VISA and MasterCard) and confirm that payments are processed successfully

3.	Auto-Generated card Number Verification
Get an automatically generated card number and verify the payment balance 
Get automatically generated card number, CVV code, expiration month and year. Card payment balance is 100 usd on default. Buy 2 items, place an order and pay with this card details, verify the payment balance after transaction. 

For all test scenarios, I have selected Selenium as the primary tool for writing automated test cases. All test cases and code changes are being uploaded to my GitHub repository. You ca review the test scenarios with steps for each test case below. 

TEST SCENARIOS 

1.	Quantity Payment Verification 

Test Case 1. 
-	Open URL https://demo.guru99.com/payment-gateway/purchasetoy.php
-	Choose 2 items from quantity dropdown 
-	Click “Buy now” button 
-	Wait for the page to load and go to payment page 
-	Check if the amount of payment equals to 40 usd 

Test Case 2. 
-	Open URL https://demo.guru99.com/payment-gateway/purchasetoy.php
-	Choose 4 items from quantity dropdown 
-	Click “Buy now” button 
-	Wait for the page to load and go to payment page 
-	Check if the amount of payment equals to 80 usd 



2.	Card Type Payment Verification

Test Case 3. 
-	Open URL https://demo.guru99.com/payment-gateway/purchasetoy.php
-	Choose 1 item from quantity dropdown 
-	Click “Buy now” button 
-	Wait for the page to load and go to payment page 
-	Enter VISA card number (random VISA that I was able to find has number 4111 1111 1111 1111)
-	Enter random expiration month, year and CVV code 
-	Click button “Pay” 
-	Confirm that payment is successful 

Test Case 4. 
-	Open URL https://demo.guru99.com/payment-gateway/purchasetoy.php
-	Choose 1 item from quantity dropdown 
-	Click “Buy now” button 
-	Wait for the page to load and go to payment page 
-	Enter MasterCard card number (random MC that I was able to find has number 5500 0000 0000 0004)
-	Enter random expiration month, year and CVV code 
-	Click button “Pay” 
-	Confirm that payment is successful 

3.	Auto-Generated card Number Verification
Test Case 5. 
-	Open URL https://demo.guru99.com/payment-gateway/cardnumber.php
-	Get credit card number details and convert it to text 
-	Cut only digits from credit card details 
-	Open to confirm the balance the following URL https://demo.guru99.com/payment-gateway/check_credit_balance.php
-	Enter credit card number 
-	Click button “Submit” 
-	Confirm that credit card balance shows no transaction 

 Test Case 6. 
-	Open URL https://demo.guru99.com/payment-gateway/cardnumber.php
-	Get credit card number details and convert it to text 
-	Cut only digits from credit card details, store is as text 
-	Open URL https://demo.guru99.com/payment-gateway/purchasetoy.php 
-	Purchase 2 items 
-	Click “Buy now” button 
-	Wait for the page to load and go to payment page 
-	Enter step by step credit card number, CVV code, month and year
-	Click “Pay” button 
-	Wait for page to load and confirm order and payment
-	Open to confirm the balance the following URL https://demo.guru99.com/payment-gateway/check_credit_balance.php
-	Enter credit card number 
-	Click button “Submit” 
-	Confirm that credit card balance shows transaction being just done 

