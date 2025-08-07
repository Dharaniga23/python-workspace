def happy_birthday(name,age):
    print(f"happy birthday to you {name}")
    print(f"you are {age} years old")
    print("happy birthday to you")

happy_birthday("dharan",21)
happy_birthday("bommu",20)
happy_birthday("kutty",19)

def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()

    return first +" "+last
full_name = create_name("dharaniga","subramanian")

print(full_name)