# **User manual**
## **What is SSN Validator?**
SSN Validator is a software that let the user know if the user input is a SSN, followed by the rules of the validation in this context. 

Developed in Python and testes with Pytest. This software is a simple console app and is just for the specific function described before.

## **When an SSN is Valid?**
Is valid when it meets the following requirements:
The whole text has a length of 11 characters. 9 digits and 2 hyphens (-).

It has 3 parts, divided by the hyphens:
* First part needs to be composed by 3 digits, different by 000 and 666. And not between 900 and 999.
* Second part has 2 digits, need to be different by 00 (greater). 
* Third part has 4 digits, needs to be different by 0000 (greater).
> The format of SSN is: XXX-XX-XXXX, understanding the Xs as digits.


If the SSN meets these conditions, then is a valid SSN.
## **Versions**
This is the first version of the application, therefore, 1.0. In addition, versions of programming language and framework are: 
* Python version: 3.10.4.
* Pytest version: 7.1.2.


Therefore, you need to be sure that your device supports these versions to run the program.
## **Rules of use**.
* The user needs to give an input with this format: XXX-XX-XXXX (including the hyphens).
* The user must run the program as much as the times he wants to validate different SSN (it is not a loop).
* The user must read the instructions to understand how to correctly use this program.
Installation
Using Ubuntu Linux 22, you must go to the link provided by the author (to GitHub), in any location you prefer. Be sure that you know where your file is because this location is going to be used to run the program eventually.


## **How to run it?**
1. Open the terminal using the following **command** (or any method you prefer to open it): ```CTRL + ALT + T```.
2. Look for the directory where the file (ArabicToRoma.py) is located using the cd command. For example, in this GitHub, the file is in: 
```cd \Requirements-Criteria-Cases\App\ArabicToRoman.py```.
3. Run the program using the command: ```python FILENAME.py```.

