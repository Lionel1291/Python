def multiplikation(numberOne,numberTwo):
    return numberOne * numberTwo

def division(numberOne,numberTwo):
    return numberOne / numberTwo

def addition(numberOne,numberTwo):
    return numberOne + numberTwo

def subtraktion(numberOne,numberTwo):
    return numberOne - numberTwo

def modulo(numberOne,numberTwo):
    return numberOne % numberTwo

def checkOperator(numberOne,numberTwo,operator):
    if(operator == "*"):
        print(multiplikation(numberOne,numberTwo))
    elif(operator == "/"):
        print(division(numberOne, numberTwo))
    elif (operator == "+"):
        print(addition(numberOne, numberTwo))
    elif (operator == "-"):
        print(subtraktion(numberOne, numberTwo))
    elif (operator == "%"):
        print(modulo(numberOne, numberTwo))
    else:
        print("Invalid Operator")

def main():
    numberOne = float(input("Bitte geben Sie eine Zahl ein: "))
    numberTwo = float(input("Bitte geben Sie eine weitere Zahl ein: "))
    operator = input("Bitte geben Sie einen Operator ein: ")
    checkOperator(numberOne,numberTwo,operator)

main()