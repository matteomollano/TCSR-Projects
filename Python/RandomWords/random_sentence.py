import random

print("Welcome to the gibberish maker 5000")

verbs = ["is", "are", "suffer", "was", "were", "being", "been", "be", "have", "has", "had", "do", "does", "did", "will", "would", "shall", "should"]

nouns = ["boy", "man", "girl", "doctor", "teacher", "washerman", "students", "country", "city", "street", "animal", "fan", "mobile", "cookies", "year", "month", "week"]

adjectives = ["beautful", "witty", "wicked", "confusing", "rich", "new", "strange", "rocky", "circular", "helpful", "component", "smelly", "stable", "grumpy", "devoted", "smart", "muscular", "graceful", "scary", "safe", "wooden", "sleepy", "tardy", "hungry", "strange", "hopeful", "proud", "new", "dainty", "royal", "arrogant", "round", "efficient", "youthful", "cumbersone", "fickle", "mild", "expensive", "small", "rude", "generous", "courageous", "zany", "thin", "round", "oval", "dark", "hot", "modern", "petite", "weary"]

animals = ["lion", "fish", "ferret", "goat", "crab", "wolverine", "cow", "horse", "crow", "meerkat", "seal", "llama", "leopard", "rhinoceros", "warthog", "age", "chipmunk", "elephant", "deer", "wairus", "panda"]

sentence = []

random_number = random.randint(4, 20)

# list of lists to choose from
word_lists = [verbs, nouns, adjectives, animals]

for i in range(random_number):
    # select a list randomly
    selected_list = random.choice(word_lists)
    # choose a random word from the selected list
    random_word = random.choice(selected_list)
    
    # while the random word is already in the list, choose a new word
    while random_word in sentence:
        random_word = random.choice(selected_list)
    
    # add the random word to our sentence
    sentence.append(random_word)
    
# create the sentence
print("\nOur sentence is...")
print(' '.join(sentence))