operator = input("enter an operator(+,-,*,/):")
num1 = float(input("enter the first num:"))
num2 = float(input("enter the second num:"))

if operator == "+":
   result = num1 + num2
   print(round(result,3))
elif operator == "-":
   result = num1 - num2
   print(round(result,3))
elif operator == "*":
   result = num1 * num2
   print(round(result,3))
elif operator == "/":
   result = num1 / num2
   print(round(result,3))
else:
   print("invalid operator")