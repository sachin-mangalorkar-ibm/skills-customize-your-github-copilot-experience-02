# 📘 Assignment: Games in Python

## 🎯 Objective

Build a classic Hangman game in Python using strings, loops, conditionals, and user input. By completing this assignment, you will practice designing game logic and managing game state across turns.

## 📝 Tasks

### 🛠️ Build the Core Hangman Loop

#### Description
Create the main game flow for Hangman where a hidden word is selected and the player guesses one letter at a time.

#### Requirements
Completed program should:

- Randomly select one word from a predefined list of words.
- Display the current progress of the word using underscores for unguessed letters.
- Prompt the player for a single-letter guess on each turn.
- Update and redisplay the word progress after each valid guess.

### 🛠️ Handle Win/Loss Conditions and Feedback

#### Description
Add the rules that determine when the game ends and provide clear feedback to the player.

#### Requirements
Completed program should:

- Track incorrect guesses remaining and reduce the count for wrong guesses.
- Prevent repeated guesses from incorrectly reducing remaining attempts.
- End the game with a win message when the full word is guessed.
- End the game with a loss message when attempts are exhausted, and reveal the word.
