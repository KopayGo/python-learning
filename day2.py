print("=" * 40)
print(f"Easy Calculator" .center(40))
print("=" * 40)
print()
num1 = input("Enter the first number : ")
num1 = float(num1)
num2 = input("Enter the second number : ")
num2 = float(num2)
print("\nAvailable operations : ")
print(" + ")
print(" - ")
print(" * ")
print(" / ")
print()
operation = input("choose an operation : ")
if operation == "+":
    result = num1 + num2
    print(f"\n{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"\n{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"\n{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
         result = num1 / num2
         print(f"\n{num1} / {num2} = {result:.2f}")
    else:
        print(f"\n Error!!! ")   
else:
    print("\n Error!!! ")   
print("\n" + "=" * 40)
              
