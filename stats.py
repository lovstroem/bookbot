# Accepts a text as a string and return the number of words used
def number_of_words(text):
    count = 0
    for word in text.split():
        count += 1
    return count