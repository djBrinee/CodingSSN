def SSNValidation(number):
    firsPart = number[0:3]
    SecondPart = number[4:6]
    ThirdPart = number[7:12]
    if(len(number) != 11 or (number[3] != number[6])):
        return False
    elif(firsPart.isnumeric() == False or SecondPart.isnumeric() == False or ThirdPart.isnumeric() == False):
        return False
    elif(firsPart == 000 or firsPart == 666 or (900 > int(firsPart) > 999)):
        return False
    elif(int(SecondPart) <= 0 or int(ThirdPart) <= 0000):
        return False
    else:
        return True

def Main():
    SSN = input("Please type an SSN to validate its format: ")
    if(SSNValidation(SSN)):
        return "Correct format"
    else:
        return "Incorrect format, check SSN Rules in ReadMe file"

print(Main())

