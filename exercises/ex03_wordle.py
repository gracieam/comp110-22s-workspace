"""Structured Wordle."""

___author___ = "730402215"

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"

# main will keep track of guesses and call all of the functions used
def main() -> None:
    """The entrypoint of the program and main game loop"""
    secret: str = "codes"
    turn_N: int = 1
    guess: str = ""
    is_won: bool = False
    while turn_N < 6 and is_won is False:
        print(f"=== Turn {turn_N}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            is_won = True
        turn_N += 1
    if is_won == True:
        print(f"You won in {turn_N}/6 turns! ")
    elif is_won == False:
        print("X/6 - Sorry, try again tomorrow!")

# will help emojified run properly by checking indices
def contains_char(secret: str, char_guess: str) -> bool:
    """Searches in secret_word for char_guess"""
    assert len(char_guess) == 1
    i: int = 0
    while i < len(secret):
        if char_guess != secret[i]:
            i += 1
        else:
            return True
    return False 

# gives visual representation of inidices check
def emojified(guess: str, secret: str) -> str:
    "Codifying the secret with an emoji string given the guess"
    assert len(secret) == len(guess)
    i: int = 0
    emoji: str = ""
    while i < len(secret):
        if guess[i] == secret[i]:
            emoji += green_box
        elif contains_char(secret, guess[i]):
            emoji += yellow_box
        else:
            emoji += white_box
        i += 1
    return emoji

# prompts user for a word and keeps track of the length of the word
def input_guess(expect_len: int) -> str:
    "Prompting user to provide guess of expected length"
    guess: str = input(f"Enter a {expect_len} character word: ")
    guess_length = len(guess)
    while guess_length != expect_len:
        guess = input(f"That wasn't {expect_len} chars! Try again: ")
        guess_length = len(guess)
    return guess

if __name__ == "__main__":
    main()