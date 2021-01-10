num1 = float(input("enter your 1st number :"))
op = (input("enter your operator :"))
num2 = float(input("enter your 2nd number :"))

if op == "+":
    print(num1 + num2)
    print("is the answer for addition")
elif op == "-":
    print(num1 - num2)
    print("is the answer for subtraction")
elif op == "/":
    print(num1 / num2)
    print("is the answer for division ")
elif op == "*":
    print(num1 * num2)
    print("is the answer for multiplication")
elif op == "^":
    print(pow(num1 ,num2 ))

else:
    print("invalid operation")
