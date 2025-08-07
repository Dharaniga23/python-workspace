#string
name = "dharaniga"

if "v" in name:
    print("there is a 'a'")
else:
    print("a is not present")

#list
students = ["dharaniga","kavi","aadhi"]

student =input( "enter the name of the student:")

if student in students:
    print(f"{student} is present in the list")
else:
    print(f"{student} is not present in the list")

#tuple
fruits = ("apple","orange","grapes","banana")
fruit = input("enter the name of the fruit:")

if fruit not in fruits:
    print(f"{fruit} is not present in the tuple")
else:
    print(f"{fruit} is present in the tuple")

#set
vegetables = {"carrot","potato","onion","tomato"}
vegetable = input("enter the name of the vegetable:")   
if vegetable in vegetables:
    print(f"{vegetable} is present in the set")
else:
    print(f"{vegetable} is not present in the set")

#dictionary
grades ={"dharan":"A",
         "kavi":"B",
         "aadhi":"C"}
student = input("enter the name of the student to check grade:")
if student in grades:
    print(f"{student} has a grade of {grades[student]}")
else:
    print(f"{student} is not present in the dictionary")