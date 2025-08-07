def is_fruit(fruit):
    match fruit:
        case "apple" | "banana" | "cherry":
            return "This is a fruit."
        case "potato" | "carrot" | "onion":
            return "This is a vegetable."
        case _:
            return "This is not a recognized fruit or vegetable."
        
print(is_fruit("tomato"))