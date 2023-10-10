word = "dolphin"
unique_letters = len(set(word))
counter = 0
guesses = []
correct_letters = []

while counter < unique_letters:
    guess = input("\nGuess a letter: ")
    if guess in guesses:
        print("\nYou've already guessed that letter, guess again")
        continue
    guesses.append(guess)
    if guess in word:
        print("\nYou guessed a correct letter!")
        correct_letters.append(guess)
        counter += 1
    else:
        print("\nNot a correct letter, try again")
    for letter in word:
        if letter in correct_letters:
            print(letter, end="")
        else:
            print("_", end="") 
    if counter == unique_letters:
        print("\nThe End!")