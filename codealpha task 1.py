import random


words = ["apple", "bread", "chair", "drink", "eagle"]
word = random.choice(words)
word_letters = list(word)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("Welcome to Hangman!")


while incorrect_guesses < max_incorrect:
    
    display_word = ""
    for letter in word_letters:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    print("Word: ", display_word)

    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

   
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in word_letters:
        print("Correct guess!")
        guessed_letters.append(guess)
    else:
        print("Incorrect guess.")
        guessed_letters.append(guess)
        incorrect_guesses += 1
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")


if incorrect_guesses == max_incorrect:
    print("Game over. The word was:", word)
