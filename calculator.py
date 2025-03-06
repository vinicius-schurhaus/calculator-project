def showMenu():
    print("-------------------------")
    print("|      CALCULATOR       |")
    print("-------------------------")
    print("|  0 : Add              |")
    print("|  1 : Subtract         |")
    print("|  2 : Multiply         |")
    print("|  3 : Divide           |")
    print("|  4 : Exponentiate     |")
    print("-------------------------")

def displaySelectedOption(option):
    operationDict = {0: "Add", 1: "Subtract", 2: "Multiply", 3: "Divide", 4: "Exponentiate"}
    print(f"You selected: {operationDict[option]}")

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return n1 / n2

def exponentiate(n1, n2):
    return n1 ** n2

def calculate(option, n1, n2):
    operations = [add, subtract, multiply, divide, exponentiate]
    return operations[option](n1, n2)

def showResult(n1, n2, result, option):
    operationSymbols = {0: "+", 1: "-", 2: "x", 3: "/", 4: "^"}
    if result is not None:
        print(f"{n1} {operationSymbols[option]} {n2} = {result}")
    else:
        print("Operation could not be performed.")

def askToContinue():
    while True:
        response = input("Do you want to perform another operation? (y/n): ").strip().lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

while True:
    showMenu()
    try:
        option = int(input("Choose an option: "))
        if option < 0 or option > 4:
            print("Invalid option. Please choose a number between 0 and 4.")
            continue
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    
    displaySelectedOption(option)
    
    try:
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue
    
    result = calculate(option, n1, n2)
    showResult(n1, n2, result, option)
    
    if not askToContinue():
        break
