name = input("enter your name:")

#result = len(name)
#result = name.capitalize()
#result = name.upper()
#result = name.isalpha()
#result = name.isdigit()
#result = name.rfind("a")
#print(result)
#print(help(str))

if len(name)>12:
    print("your name should not be greater than 12 characters")
elif not name.find(" ") == -1:
    print("your name should not contain spaces")
elif not name.isalpha():
    print("your name should not contain digits")
else:
    print(f"welcome {name}")
    