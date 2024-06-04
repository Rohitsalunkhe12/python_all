import random

words = ['rahul', 'lahur', 'sawant', 'wasant', 'rohit', 'hitro', 'bat', 'tab']
score = 0
wrong_guesses = {}

while True:
    chosen_word = random.choice(words)
    letters = list(chosen_word)
    random.shuffle(letters)
    print("Guess the correct word:", " ".join(letters))
    user_word = input("Write the correct word or type 'Quit' to end the game: ").strip().lower()

    if user_word == 'quit':
        break

    if sorted(user_word) == sorted(chosen_word) and user_word in words:
        score += len(user_word)
        print(f"Correct! Your score is now: {score}")
        wrong_guesses.clear()  # Clear the wrong guesses since the player got it right
    else:
        if user_word in wrong_guesses:
            wrong_guesses[user_word] += 1
        else:
            wrong_guesses[user_word] = 1

        if wrong_guesses[user_word] >= 3:
            print(f"You have reached the limit for the word '{user_word}'.")
        else:
            print("Wrong word. Try again.")

print(f"Game over. Your final score is: {score}")
