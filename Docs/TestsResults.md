# **Testing results documentation**

## **1. Check if the program validates the range of the first part in the SSN**
### **Flow**
* Function to test: SSNValidation
* Inputs: 000-25-6302, 666-25-6302, 920-25-6302 and 250-25-6302
* Expected results: False, False, False, True
* Real Results: False, False, False, True
* Conclusion: Scenario Working

## **2. Validate if the program validates the range of the second part in SSN**
### **Flow**
* Function to test: SSNValidation
* Inputs: 250-00-9520, 250-20-9520
* Expected results: False, True
* Real Results: False, True
* Conclusion: Scneario Working

## **3. Check if the program validates the format in SSN (divided by hyphen)**
### **Flow**
* Function to test: SSNValidation
* Input: 250*20*5000
* Expected result: False
* Real Result: False
* Conclusion: Scneario Working

## **4. Confirm if the program support incorrect inputs (random strings, special characters, etc.)**
### **Flow**
* Function to test: SSNValidation
* Input: Juan Gabriel 
* Expected result: False
* Real Result: False
* Conclusion: Scenario Working

## **5. Verify if the program validates the range of the third part in SSN**
### **Flow**
* Function to test: SSNValidation
* Inputs: 250-20-5000, 250-20-0000
* Expected results: True, False
* Real Results: True, False
* Conclusion: Scenario Working