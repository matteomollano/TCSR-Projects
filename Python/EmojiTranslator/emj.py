import emoji
from sentence_transformers import SentenceTransformer, util

emoji_list = []
emoji_names = []

for emj, metadata in emoji.EMOJI_DATA.items():
    name = metadata['en']
    name = name[1:-1]
    emoji_list.append(emj)
    emoji_names.append(name)

model = SentenceTransformer('all-MiniLM-L6-v2')

# convert emoji names to embeddings
emoji_embeddings = model.encode(emoji_names, convert_to_tensor=True)

# take a word from the sentence -> return the best emoji
def find_best_emoji(word):
    word_lower = word.lower()
    word_embedding = model.encode(word_lower, convert_to_tensor=True)
    similarities = util.cos_sim(word_embedding, emoji_embeddings)[0]
    best_idx = similarities.argmax().item()
    # print(emoji_list[best_idx])
    
    best_score = similarities[best_idx].item()
    if best_score > 0.40:  # adjust as needed
        return emoji_list[best_idx]
    else:
        return word  # fallback to the original word
    
find_best_emoji("I")

"I like pizza -> ['I', 'like', 'pizza']"
# loop over the list, call find_best_emoji on each word
# join everything together using " ".join()
def translate_sentence(sentence):
    words = sentence.split()
    translated = []
    
    for word in words:
        emj = find_best_emoji(word)
        translated.append(emj)
    
    return " ".join(translated)

while True:
    user_input = input("Enter a sentence: ")
    result = translate_sentence(user_input)
    print(f"Translated: {result}\n")