import emoji
from sentence_transformers import SentenceTransformer, util

# [(emoji1, name1), (emoji2, name2), ...]
emoji_list = []
# [name1, name2, name3, name4, ...]
emoji_names = []
for emj, info in emoji.EMOJI_DATA.items():
    name = info['en']
    name = name.replace(":", "")
    item = (emj, name)
    emoji_list.append(item)
    emoji_names.append(name)

# model = SentenceTransformer('all-MiniLM-L6-v2')
model = SentenceTransformer('all-mpnet-base-v2')
# sentence = ['I', 'love', 'pizza']
# embeddings = model.encode(sentence, convert_to_tensor=True)
# print(embeddings)

# convert emoji names to embeddings
emoji_embeddings = model.encode(emoji_names, convert_to_tensor=True)

# word -> find the best emoji for it
def find_best_emoji(word):
    word_lower = word.lower()
    word_embedding = model.encode(word_lower, convert_to_tensor=True)
    similarity = util.cos_sim(word_embedding, emoji_embeddings)[0]
    # print(similarity)
    # print(f"Length of similarity: {len(similarity)}")
    best_idx = similarity.argmax().item()
    # print(best_idx)
    
    best_score = similarity[best_idx].item()
    if best_score > 0.40:  # adjust as needed
        return emoji_list[best_idx][0]
    else:
        return word  # fallback to the original word
    
find_best_emoji("pizza")

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