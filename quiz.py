questions = ("which is my favourite color?",
             "what is ur nickname?",
             "which do you like the most?",
             "how old are you?")

choices = (("A.red","B.pink","C.purple","D.yellow"),
           ("A.bommu","B.dharaniga","C.dharani","D.dharan"),
           ("A.pizza","B.waffles","C.falooda","D.shawarma"),
           ("A.20","B.19","C.18","D.21"))


answers = ("C","A","B","D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for choice in choices[question_num]:
        print(choice)
    guess = input("enter your guess(A,B,C,D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("answer is correct")
        score +=1
    else:
        print("answer is incorrect")
        print(f"{answers[question_num]} is the correct answer")
    question_num +=1

print("----------------------")
print("       SCORES       ")
print("----------------------")

print("answers:",end=" ")
for answer in answers:
    print(answer,end=" ")
print()

print("guesses:",end=" ")
for guess in guesses:
    print(guess,end=" ")
print()

score = int(score / len(questions)*100)
print(f"your score is: {score}")



