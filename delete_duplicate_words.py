
def delete_duplicate_words(text):
    words_list = text.split(" ")
    unique_words = []
    
    for word in words_list:
        if word not in unique_words:
            unique_words.append(word)
    
    return " ".join(unique_words)

input_text = "This is a test for testing unique words in a sentence. This is just a test. This test contains more repetition than the previous one."

     
print(delete_duplicate_words(input_text))


