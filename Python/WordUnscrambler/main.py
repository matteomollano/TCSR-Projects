import random

def scramble_word(word):
    """Return a scrambled version of a word."""
    letters = list(word)
    random.shuffle(letters)
    return ''.join(letters)

def play_word_scrambler(words):
    # pick a random word
    word = random.choice(words)
    scrambled = scramble_word(word)

    print("Welcome to Word Scrambler!")
    print(f"Here's your scrambled word: {scrambled}")
    print("Try to guess the original word!\n")

    while True:
        guess = input("Your guess: ").strip().lower()

        if len(guess) != len(word):
            print(f"Guess must be {len(word)} letters long.\n")
            continue

        # check for win
        if guess == word:
            print("Correct! You unscrambled the word!")
            break

        # give feedback (green background if correct spot)
        feedback = []
        for i in range(len(word)):
            if guess[i] == word[i]:
                feedback.append("\033[42m" + guess[i] + "\033[0m")  # green background
            else:
                feedback.append(guess[i])

        print("Feedback: " + "".join(feedback) + "\n")


# Example usage
words = ["python", "jumble", "scramble", "computer", "science"]
play_word_scrambler(words)