"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730402215"

word_guess: str = input("Enter a 5-character word: ")
word_guess_length = len(word_guess)
if word_guess_length != 5:
    print("Error: Word must contain 5 characters")
    quit()  
letter_guess: str = input("Enter a single character: ")
letter_guess_length = len(letter_guess)
if letter_guess_length != 1:
    print("Error: Character must be a single character. ")
    quit()
print("Searching for " + letter_guess + " in " + word_guess)

first_letter: str = word_guess[0]
second_letter: str = word_guess[1]
third_letter: str = word_guess[2]
fourth_letter: str = word_guess[3]
fifth_letter: str = word_guess[4]

counter = 0

if letter_guess == first_letter:
    print(letter_guess + " found at index 0")
    counter = counter + 1
if letter_guess == second_letter:
    print(letter_guess + " found at index 1")
    counter = counter + 1
if letter_guess == third_letter:
    print(letter_guess + " found at index 2")
    counter = counter + 1
if letter_guess == fourth_letter:
    print(letter_guess + " found at index 3")
    counter = counter + 1
if letter_guess == fifth_letter:
    print(letter_guess + " found at index 4")
    counter = counter + 1

counter_str = str(counter)
print(counter_str + " instances of " + letter_guess + " found in " + word_guess)