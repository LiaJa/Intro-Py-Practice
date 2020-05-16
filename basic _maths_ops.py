x = int(input("Enter number for x:"))
y = int(input("Enter number for y:"))

operation = input("Select math operation: +, -, * or /:")

if operation == "+":
    print(x+y)

elif operation == "-":
    print(x-y)

elif operation == "*":
    print(x*y)

elif operation == "/":
    print(x/y)

else:
    print("Math error occured!")