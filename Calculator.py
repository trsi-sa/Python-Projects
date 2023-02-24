num1 = float(input("Enter The Frist Number :"))
operator = input("Enter The Operator :")
num2 = float(input("Enter The Second Number :"))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
else:
    print("Wrong Operactor Please Try Again")