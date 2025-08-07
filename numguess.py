import random

low = 1
high = 50
guesses = 0
is_running = True

answer = random.randint(low,high)

print("NUMBER GUESSING GAME")
print(f"Select a number between {low} and {high}")

while is_running:
    guess = input("Enter a guess:")

    if guess.isdigit():
        guess = int(guess)
        guesses +=1
        
        if guess < low or guess > high:
            print("That number is out of range")
            print(" Please enter a number between {low} and {high}:")
        elif guess< answer:
            print("Too low,try again")
        elif guess> answer:
            print("Too high,try again")
        else:
            print("Correct guess")
            print(f"the correct answer is {answer}")
            print(f"The number of guesses: {guesses}")
            
            is_running=False
    else:
        print(f"{guess} is not valid")
        print(" Please enter a number between {low} and {high}:")
