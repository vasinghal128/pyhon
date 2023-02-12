First = input("Enter your first Digit")

Second = input("Enter your second Digit")

print("if you want add Digits press +")

add = float(First) + float(Second)

print("if you want subtract Digits press -")

subtract = float(First) - float(Second)

print("if you want multiply Digits press *")

multiply = float(First) * float(Second)

print("if you want divide two Digits press /")

divide = float(First) / float(Second)

print("if you want reminder of Digits press %")

reminder = float(First) % float(Second)

press = input("press + , - , * , / , % ")

if press == "+":
    print(float(add))

elif press == "-":
    print(float(subtract))

elif press == "*":
    print(float(multiply))

elif press == "/":
    print(float(divide))

elif press == "%":
    print(float(reminder))

else:
    print("Enter right operator")