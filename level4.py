import random
words = ["mountain", "dolphin", "snow", "forest", "ocean", "lifeguard", "umbrella", "planet", "atmosphere", "building", "canal", "tugboat", "cliff", "pie", "goat", "ear", "maze", "zoom", "xylophone", "responsive", "pneumonia"]

easy = []
medium = []
hard = []

for word in words:
    if len(word) < 6:
        easy.append(word)
    elif len(word) < 9:
        medium.append(word)
    else:
        hard.append(word)

level_choice = False; 
word = ""
tries = 0

def getWord(lev):
    random_num = random.randint(0, len(lev)-1)
    return lev[random_num]

while (level_choice == False):
    level = input("Select your difficulty level (easy, medium, or hard): ")
    if level == "easy":
        word = getWord(easy)
        level_choice = True
        tries = 8
    elif level == "medium":
        word = getWord(medium)
        level_choice = True
        tries = 11
    elif level == "hard":
        word = getWord(hard)
        level_choice = True
        tries = 14
    else:
        print("Not a valid selection")


unique_letters = len(set(word))
counter = 0
guesses = []
correct_letters = []

for letter in word:
    print("_", end="")
print(f"\nNumber of tries: {tries}")

while counter < unique_letters and tries > 0:
    guess = input("\nGuess a letter: ")
    if guess in guesses:
        print("\nYou've already guessed that letter, guess again")
        continue
    guesses.append(guess)
    if guess in word:
        print("\nYou guessed a correct letter!")
        correct_letters.append(guess)
        counter += 1
        tries -= 1
    else:
        print("\nNot a correct letter, try again")
        tries -= 1
    for letter in word:
        if letter in correct_letters:
            print(letter, end="")
        else:
            print("_", end="") 
    print(f"\nNumber of tries left: {tries}")
    if tries == 0:
        print("\nOut of tries. Play again")
    if counter == unique_letters:
        print("\nYou win!")