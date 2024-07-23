 I have prepared 3 test scenarios for training website https://demo.guru99.com/payment-gateway/purchasetoy.php
 I have created 3 test scenarios with 2 test cases for each. Test scenarios and test cases with steps you can check below on this page. While testing basic internet shop, I have come up with idea to test the following parts of purchasing: 1) buy 2 and 4 items and confirm that amount of payment is being changed accordingly; 2) check payments with two different types of cards (VISA and MasterCard) and confirm that payment is done successfully; 3) get automatically generated card number and check the payment balance; get automatically generated card number with credit limit 100 usd, pay using this card, check the balance after transaction. 
For all test scenarios I have chosen Selenium as a main tool for writing automated test cases. All test cases and changes in code are being downloaded to my github repository.  
Test scenarios, test cases and steps of each test you can check below.  
Test scenarios
1.	Purchasing several items 
1.	
-	Open the URL (https://demo.guru99.com/payment-gateway/purchasetoy.php ) 
-	Choose 2 items from quantity dropdown 
-	Click the button “Buy now” 
-	Wait for the page to load and switch to payment page 
-	Check if the amount equals to 40usd. 
2.	 
-	Open the URL (https://demo.guru99.com/payment-gateway/purchasetoy.php ) 
-	Select 4 items from quantity dropdown 
-	Click the button “Buy now” 
-	Wait for the page to load and switch to payment page 
-	Check if the amount equals to 80usd. 

2.	Payment automation test
3.	
-	Open the URL (https://demo.guru99.com/payment-gateway/purchasetoy.php ) 
-	Select 1 item from quantity dropdown 
-	Click the button “Buy now” 
-	Wait for the page to load and switch to payment page 
-	Enter VISA credit card details (card number, expiration moth, expiration year, CVV code)
-	Click button pay
-	Confirm that payment is successful. 
4.	 
-	Open the URL (https://demo.guru99.com/payment-gateway/purchasetoy.php ) 
-	Select 1 item from quantity dropdown 
-	Click the button “Buy now” 
-	Wait for the page to load and switch to payment page 
-	Enter VISA credit card details (card number, expiration moth, expiration year, CVV code)
-	Click button pay
-	Confirm that payment is successful. 
Payment automation test
5.	
-	Get automatically generated credit card details from URL https://demo.guru99.com/payment-gateway/cardnumber.php
-	Go to the following URL https://demo.guru99.com/payment-gateway/check_credit_balance.php
-	Check the credit card balance 
-	Confirm that no transfers have been done 
6.	
-	Get automatically generated credit card details from URL https://demo.guru99.com/payment-gateway/cardnumber.php
-	Open the URL (https://demo.guru99.com/payment-gateway/purchasetoy.php ) 
-	Select 1 item from quantity dropdown 
-	Click the button “Buy now” 
-	Wait for the page to load and switch to payment page 
-	Enter saved credit card details (card number, expiration moth, expiration year, CVV code)
-	Click button pay
-	Confirm that payment is successful.
-	Go to the following URL https://demo.guru99.com/payment-gateway/check_credit_balance.php
-	Check the credit card balance 
