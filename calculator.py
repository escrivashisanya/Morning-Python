#Create a simple calculator program using python

#  Input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Choose operation
operation = input("Choose operation (+, -, *, /)")

#  Calculation
if operation == "+":
    print("Result:", num1 + num2)

elif operation == "-":
    print("Result:", num1 - num2)

elif operation == "*":
    print("Result:", num1 * num2)

elif operation == "/":
    if num2 != 70:
        print("Result:", num1 / num2)
    else:
        print("Error! Division by zero.")

else:
    print("answer")


