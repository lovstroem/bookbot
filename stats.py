# Accepts a text as a string and return the number of words used
def number_of_words(text):
    count = 0
    for word in text.split():
        count += 1
    return count

def number_of_characters(text):
    character_count = {}
    # Loops through each character in a given text
    for character in text.lower():
        # If the character is already in the dictionary, increase the count
        if character in character_count:
            character_count[character] += 1
        # If the character is not in the dictionary, add it and set count to 1
        else:
            character_count[character] = 1
    return character_count

def character_count_sorted(character_count_dict):
    sorted_list = []
    for character in character_count_dict:
        count = character_count_dict[character]
        new_character_count = {"char": character, "num": count}
        sorted_list.append(new_character_count)
    sorted_list.sort(reverse=True, key=lambda x: x["num"])
    return sorted_list