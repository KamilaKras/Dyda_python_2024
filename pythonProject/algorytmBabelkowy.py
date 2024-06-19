#KALKULATOR
import math
def add(a, b):
    result = a + b
    return result

def subtract(a, b):
    result = a - b
    return result

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
     return a / b
    else:
        return "Cannot divide by zero!"

while True:
    print("\n")
    print("Welcome to the Kalkulator! Choose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("To exit, type 'end'")

    operation = input("Enter your choice: ")

    if operation == "end":
        print("\nGoodbye!")
        break

    if operation in ["1", "2", "3", "4"]:
        print("\nGreat")
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        if operation == "1":
            print(f"Add result:  {add(number1, number2)}")
        elif operation == "2":
            print(f"Subtract result:  {subtract(number1, number2)}")
        elif operation == "3":
            print(f"Multiply result:  {multiply(number1, number2)}")
        elif operation == "4":
            print(f"Divide result:  {divide(number1, number2)}")
    else:
        print("Invalid option! Please choose again.")
