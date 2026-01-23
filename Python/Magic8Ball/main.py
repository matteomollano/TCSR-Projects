# Magic 8 Ball
import random
import time

def get_response():
    responses = [
        "I refuse to answer you.",
        "Yes, definitely.",
        "Sources are saying no.",
        "Ask again later.",
        "Sorry, I don't know the answer to that.",
        "Cristan Ronald will break into your house at noon!",
        "Don't count on it",
    ]
    return random.choice(responses)

def main():
    while True:
        question = input("I am Magic 8 Ball! Ask me anything or q to quit: ").lower().strip()
        if question == "q":
            print("Game ending ...")
            break
        if question == "":
            print("Please ask a real question.")
            continue
        response = get_response()
        print("Magic 8 Ball says:", response, "\n")
        time.sleep(1)

if __name__ == "__main__":
    main()