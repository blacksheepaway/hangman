import random

def hangman():
    # list of possible words to guess
    saints = ["Francis", "Clare", "Thérèse", "Bernadette", "Teresa", "Joan", "Augustine", "Thomas", "Patrick", "Anthony", "Agatha", "Ambrose", "Andrew", "Angela", "Anne", "Basil", "Bede", "Benedict", "Bonaventure", "Catherine", "Christopher", "Clement", "Cyprian", "Damian", "Dominic", "Edith", "Elizabeth", "Faustina", "Gabriel", "George", "Gerard", "Gregory", "Hedwig", "Ignatius", "Isidore", "Jerome", "John", "Joseph", "Kateri", "Lawrence", "Lucy", "Luke", "Margaret", "Martha", "Martin", "Mary", "Matilda"]


    # select a random word from the list
    word = random.choice(saints).lower()

    # set up the game
    progress = "_" * len(word)
    guessed = []
    attempts_left = 6
    hangman_art = ["""
  +---+
  |   |
      |
      |
      |
      |
=========""", """
  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]

    print("Let's play Hangman!")
    print(hangman_art[0])
    print(progress)
    print("Guessed letters: ")

    while attempts_left > 0 and "_" in progress:
        guess = input("Guess a letter: ").lower()

        # check if the letter has already been guessed
        if guess in guessed:
            print(f"You already guessed '{guess}'!")
            continue

        # add the letter to the list of guessed letters
        guessed.append(guess)

        # check if the letter is in the word
        if guess in word:
            print(f"'{guess}' is in the word!")
            for i in range(len(word)):
                if word[i] == guess:
                    progress = progress[:i] + guess + progress[i+1:]
            print(hangman_art[6-attempts_left])
            print(progress)
            print("Guessed letters: ", end="")
            for letter in guessed:
                print(letter, end=" ")
            print("\n")
        else:
            print(f"'{guess}' is not in the word.")
            attempts_left -= 1
            print(hangman_art[6-attempts_left])
            print(progress)
            print("Guessed letters: ", end="")
            for letter in guessed:
                print(letter, end=" ")
            print("\n")

    # game over message
    if "_" not in progress:
        print(f"Congratulations! You guessed the word '{word}'!")
    else:
        print(f"Game over. The word was '{word}'.")

hangman()
