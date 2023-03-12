<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
</head>
<body>
	<h1>Hangman Game</h1>

<h2>Description</h2>

<p>Welcome to the classic Hangman game, where you have to guess the name of a saint before the hangman gets hanged! This program is a Python implementation of the game, where you are given a list of possible saint names and have to guess one letter at a time. With each incorrect guess, the hangman drawing gets one step closer to completion. You have a limited number of attempts to guess the word correctly, so choose wisely!</p>

<h2>How it Works</h2>

<p>When the program is executed, a random saint name is selected from the list of saints using the <code>random</code> module. The word is then displayed as underscores, with each underscore representing a letter in the word. You are prompted to enter a letter and the program checks if the letter is in the word. If the letter is correct, it is displayed in the word and the hangman drawing is updated to reflect the number of attempts remaining. If the letter is incorrect, the number of attempts remaining is reduced and the hangman drawing is updated. The game continues until you have guessed the word correctly or until the hangman is fully drawn.</p>

<h2>Techniques Used</h2>
<p>This Hangman game was written in Python and incorporates a variety of programming techniques to provide a fun and engaging user experience. Here are some of the key techniques used:</p>
<ul>
  <li>Random selection: The game randomly selects one of many Catholic saints for the user to guess. This ensures that each game is unique and challenging.</li>
  <li>String manipulation: The program uses string manipulation techniques to create the "progress" variable, which represents the current state of the word being guessed. As the user correctly guesses letters, the program updates the "progress" variable to reflect the new state of the word.</li>
  <li>Looping: The game utilizes a while loop to allow the user to continue guessing letters until either they correctly guess the word or they run out of attempts.</li>
  <li>Lists and conditionals: The game uses lists and conditionals to keep track of the letters the user has guessed and to determine whether a guessed letter is in the word.</li>
  <li>Input gathering: The program prompts the user to guess a letter and stores their input in a variable. If the letter has already been guessed, the program will inform the user and prompt them to guess again.</li>
  <li>Conditional statements: The game uses conditional statements to determine whether a guessed letter is in the word and to update the game state accordingly.</li>
  <li>ASCII art: The game uses ASCII art to display the hangman figure as the user makes incorrect guesses.</li>
</ul>
<p>Overall, this game demonstrates the power and versatility of the Python programming language, and highlights some of the fundamental techniques used in game development.</p>

<h2>Example Output</h2>

<pre><code>
Guess a letter: t
't' is not in the word.
  +---+
  |   |
  O   |
 /|   |
 /    |
      |
=========
f r a n _ _ 

Guessed letters: a e i o u f r n c t

Guess a letter: s
's' is not in the word.
  +---+
  |   |
  O   |
 /|   |
 / \  |
      |
=========
f r a n _ _ 

Guessed letters: a e i o u f r n c t s

Game over. The word was 'Francis'.
</code></pre>

<h2>Contributing</h2>

<p>If you want to contribute to this Hangman game, you can fork the repository and create a pull request with your changes. Before submitting your changes, make sure to test the game thoroughly and adhere to the existing code style.</p>

<h2>License</h2>

<p>This project is licensed under the MIT License - see the <a href="LICENSE.md">LICENSE.md</a> file for details.</p>

	// Just kidding, no JavaScript needed for this project!

</body>
</html>
