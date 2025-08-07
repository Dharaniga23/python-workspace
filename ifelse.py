age = int(input("enter your age:"))

if age>=18:
    print("you are eligible to drive cars")
elif age<=0:
    print("you are not born yet")
else:
    print("you should be 18+ to drive a car")

name = input("enter ur name :")

if name == "":
    print("you should enter your name ..can you do that")
else:
    print(f"welcome {name}")