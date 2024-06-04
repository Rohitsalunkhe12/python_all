import random

words=['rahul','lahur','sawant','wasant','rohit','hitro','bat','tab']
score=0
wrong_guesses = {}

while True:
    letters=list(random.choice(words))
    print("gase the correct word :>"," ".join(letters))
    user_word=input("write the correct word or ('Quit the game'):>")

    if user_word =='Quit':
        break

    valid = True
    for letter in user_word:
        if letter in letters:
            letters.remove(letter)

        else:
            valid = False
            break
    if valid and user_word in words:
        score = score + len(user_word)
        print(f"your score is :>{score}")
    else:
        print("wrong word")
        print("your final score",score)
