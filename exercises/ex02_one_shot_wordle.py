"""EX02 - One Shot Wordle"""

__author__ = 730402215

secret_word: str = "python"
secret_word_length = len(secret_word)
word_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
word_guess_length = len(word_guess)
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"
i = 0
emoji: str = ""
char_location: bool = False
secret_alt_i = 0


while word_guess_length != secret_word_length:
    word_guess: str = input(f"That was not {len(secret_word)} letters! Try again: ")
    word_guess_length = len(word_guess)

while i < secret_word_length:
    if word_guess[i] == secret_word[i]:
        emoji = emoji + green_box
    else:
        while secret_alt_i < secret_word_length:
            if secret_word[secret_alt_i] == word_guess[i]:
                char_location = True  
                secret_counter =+ 1
                if char_location == True:
                    emoji = emoji + yellow_box
            secret_alt_i += 1
        if char_location == False:
            emoji = emoji + white_box
    secret_alt_i = 0
    char_location = False
    i = i + 1
    
print(emoji)

if word_guess == secret_word:
    print("Woo! You got it! ")
else:
    print("Not quite. PLay again soon! ")