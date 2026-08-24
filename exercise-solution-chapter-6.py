words = ["sun", "planet", "mountain", "light", "tea"]

def has_more_than_3_characters(word):
    return len(word) > 3

filtered_words = list(filter(has_more_than_3_characters, words))
print(filtered_words) # ['planet', 'mountain', 'light']
