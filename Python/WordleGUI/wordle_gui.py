import random
from rich.console import Console
from rich.theme import Theme
from string import ascii_letters, ascii_uppercase
import contextlib

console = Console(width=50, theme=Theme({"warning": "red on yellow"}))

def main():
    
    # read content from words.txt and choose a random word
    with open("words.txt", "r") as file:
        word_list = file.read().split("\n")
        word_list = list(map(lambda word: word.upper(), word_list))
        word = random.choice(word_list)
        
    guesses = ["_" * 5] * 6
    # guesses looks like -> ['_____', '_____', '_____', '_____', '_____', '_____']
        
    # main loop
    with contextlib.suppress(KeyboardInterrupt):
        for i in range(6):
            refresh_page(f"Guess {i + 1}")
            show_guesses(guesses, word)
            
            # guesses[0:i] -> only pass the list of guesses that have been filled already
            guesses[i] = guess_word(previous_guesses=guesses[0:i])
            #guesses[i] = input(f"\nGuess {i + 1}: ").upper()
            #guesses[i] = validate_guess(guesses[i])
            
            if guesses[i] == word:
                break
    
    # returns true if last entered word == random word
    # returns false otherwise
    guessed = guesses[i] == word        
    game_over(guesses,word,guessed)

# get the user's guess and validate their input
def guess_word(previous_guesses):
    guess = console.input("\nGuess word: ").upper()
    if guess in previous_guesses:
        console.print(f"You've already guessed {guess}.", style="warning")
        return guess_word(previous_guesses)
    if len(guess) != 5:
        console.print("Your guess must be 5 letters.", style="warning")
        return guess_word(previous_guesses)
    for letter in guess:
        if letter not in ascii_letters:
            console.print(f"Invalid letter: {letter}. Please use English letters only.", style="warning")
            return guess_word(previous_guesses)
    return guess

# display user's guesses
def show_guesses(guesses, word):
    letter_status = {letter: letter for letter in ascii_uppercase}
    for guess in guesses:
        styled_guess = list()
        for letter, correct in zip(guess,word):
            if letter == correct: # if letter is correct
                style = "bold white on green"
            elif letter in word:  # if letter is misplaced
                style = "bold white on yellow"
            elif letter in ascii_letters: # if letter is wrong
                style = "white on #666666"
            else: # other letters
                style = "dim"
            styled_guess.append(f"[{style}]{letter}[/]")
            if letter != "_":
                letter_status[letter] = f"[{style}]{letter}[/]]"
        console.print("".join(styled_guess), justify="center")
    console.print("\n" + "".join(letter_status.values()), justify="center")
    
# refresh the page
def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue]:leafy_green: {headline} :leafy_green:[/]\n")

# display game over message
def game_over(guesses, word, guessed_correctly):
    refresh_page("Game Over")
    show_guesses(guesses, word)
    
    if guessed_correctly:
        console.print(f"\n[bold white on green]Good job! The word is {word}.[/]")
    else:
        console.print(f"\n[bold white on red]Nice try. The word was {word}.[/]")

if __name__ == "__main__":
    main()