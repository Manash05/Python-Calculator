import time

def add(number1, number2):
    return number1 + number2

def substract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    return number1 / number2

print("\n\t--ARITHMETIC CALCULATOR--")

repeat = 1

while repeat == 1:
    print("Choose from the following operations-\n"
            "\t1. Addition.\n"
            "\t2. Substraction.\n"
            "\t3. Multiplication.\n"
            "\t4. Division.\n")

    choice = int(input("Please enter your choice: "))

    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    if choice == 1:
        print("\t", number1, "+", number2, "=", add(number1, number2), "\n")

    elif choice == 2:
        print("\t", number1, "-", number2, "=", substract(number1, number2), "\n")

    elif choice == 3:
        print("\t", number1, "*", number2, "=", multiply(number1, number2), "\n")

    elif choice == 4:
        print("\t", number1, "/", number2, "=", divide(number1, number2), "\n")

    else:
        print("Wrong Input.")

    time.sleep(0.5)

    repeat = int(input("Enter '1' to continue.\n"
                        "Enter '2' to exit.\n"))

    if repeat == 2:
        print("\t--Thank You--")