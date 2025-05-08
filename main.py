from stats import number_of_words, number_of_characters, character_count_sorted

# Reads a file and returns the text as a string
def get_book_text(book):
    with open (book) as f:
        book_content = f.read()
    return book_content

def main():
    word_count = number_of_words(get_book_text("books/frankenstein.txt"))
    character_count = number_of_characters(get_book_text("books/frankenstein.txt"))
    sorted_count = character_count_sorted(character_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_count:
        if item["char"].isalpha() == True:
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

#sorted_list.sort(reverse=True, key=lambda x: x["num"])

main()