import random


words = {
    "python": "Programming language",
    "apple": "A fruit",
    "cricket": "Popular sport",
    "laptop": "Electronic device"
}


word = random.choice(
    list(words.keys())
)

hint = words[word]

guessed = []

attempts = 6


print("Welcome to Hangman")
print("Hint:", hint)


while attempts > 0:

    display = ""

    for letter in word:

        if letter in guessed:
            display += letter

        else:
            display += "_"


    print("\nWord:", display)


    if display == word:
        print("You won!")
        break


    guess = input(
        "Enter letter: "
    )


    if guess in guessed:
        print("Already guessed")
        continue


    guessed.append(guess)


    if guess not in word:

        attempts -= 1

        print(
            "Wrong guess"
        )

        print(
            "Attempts left:",
            attempts
        )


else:
    print(
        "Game Over"
    )

    print(
        "Word was:",
        word
    )