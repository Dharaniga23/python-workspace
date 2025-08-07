foods = []
prices = []
total =  0

while True:
     food = input("Enter the food u like to order(q to quit):")
     if food.lower()== "q":
          break
     else:
          price = float(input("Enter the price of the food:$"))
          foods.append(food)
          prices.append(price)
print()

print("*********YOUR CART*********")  

for food in foods:
     print(food, end=" ")

print()

for price in prices:
     total+=price

print(f"Your total is: $ {total}")

