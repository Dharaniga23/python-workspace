#print("hello world")
#variables
myname="Dharaniga"
myage=21
mycgpa=8.50
is_student=False
print(f"my name is {myname}")
print(f"i am {myage} years old")
print(f"i have a cgpa of {mycgpa}")
if is_student:
    print("you are a student")
else:
    print("you are not a student")

myage=float(myage)
print(myage)

myage=str(myage)
print(myage)

print(type(myage))

#typecasting

age = int(input("enter your age:"))
print(f"yeah you are {age} years old")

length=float(input("enter the length:"))
width=float(input("enter the width:"))
area= length * width
print(f"the area is {area}cm²")