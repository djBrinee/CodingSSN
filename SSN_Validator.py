"""
Program to validate SSN.
By: Deivy Peña. ID: 1099429.

SSN Format:
DDD-DD-DDDD
Rules:
* First Part: != 000 and != 666 and ~(900, 999)
* Second Part: > 00
* Third Part: > 0000
"""

#Function to validate SSN though conditions
def SSNValidation(number):
    FirstPart = number[0:3]
    SecondPart = number[4:6]
    ThirdPart = number[7:12]
    if(len(number) != 11 or number[3] != "-" or number[6] != "-"):
        return False
    elif(FirstPart.isnumeric() == False or SecondPart.isnumeric() == False or ThirdPart.isnumeric() == False):
        return False
    elif(int(FirstPart) == 000 or int(FirstPart) == 666 or ( 900 < int(FirstPart) < 999)):
        return False
    elif(int(SecondPart) <= 0 or int(ThirdPart) <= 0):
        return False
    else:
        return True

# Functionr that works as a Main method
def Main():
    SSN_Number = input("Type your SSN to validate it: ")
    if(SSNValidation(SSN_Number)):
        return "Correct Format!"
    else:
        return "Incorrect Format, check the rules at User Manual Document!"

print(Main())
