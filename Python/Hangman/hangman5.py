import requests

def get_random_word():
    response = requests.get("https://randomapi.dev/api/words?count=1").json()
    return response['data'][0]['word']

def get_letter():
    guess = input("Guess a letter: ")
    return guess

def main():
    random_word = get_random_word()
    underscores = ["_"] * len(random_word)
    letter_bank = []

    current_word = " ".join(underscores)
    print(current_word)

    guess = get_letter()
    while guess in letter_bank:
        guess = get_letter()

    letter_bank.append(guess)

    for i in range(len(random_word)):
        if guess == random_word[i]:
            underscores[i] = guess

    current_word = " ".join(underscores)
    print(current_word)
    print(f"\n Letter bank: {letter_bank}")


if __name__ == "__main__":
    main()
