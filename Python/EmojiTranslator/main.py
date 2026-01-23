import emoji
from sentence_transformers import SentenceTransformer, util

# model = SentenceTransformer('all-MiniLM-L6-v2')  # lightweight and fast
model = SentenceTransformer('all-mpnet-base-v2')

emoji_list = []
for emj, info in emoji.EMOJI_DATA.items():
    if 'en' in info:
        name = info['en']
        emoji_list.append((name, emj))

# Precompute emoji description vectors
emoji_names = [name for name, _ in emoji_list]
emoji_vectors = model.encode(emoji_names, convert_to_tensor=True)

def find_best_emoji(word):
    word_lower = word.lower()
    word_vector = model.encode(word_lower, convert_to_tensor=True)
    similarity = util.cos_sim(word_vector, emoji_vectors)[0]
    best_idx = similarity.argmax().item()
    # argmax() gets the index of the maximum similarity value
    # item() is used to pull the Python integer out of the tensor object
    
    best_score = similarity[best_idx].item()
    if best_score > 0.35:  # adjust as needed
        return emoji_list[best_idx][1]
    else:
        return word  # fallback to the original word

    # return emoji_list[best_idx][1]

def translate_sentence(sentence):
    words = sentence.split()
    translated = []

    for word in words:
        try:
            emoji_char = find_best_emoji(word)
            translated.append(emoji_char)
        except:
            translated.append(word)
    
    return " ".join(translated)

# --- Main Program ---
print("🧠 Semantic Emoji Translator!")
while True:
    user_input = input("Type a sentence: ")
    result = translate_sentence(user_input)
    print("Translated:", result)
    print()