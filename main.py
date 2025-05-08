from stats import number_of_words, number_of_characters

# Reads a file and returns the text as a string
def get_book_text(book):
    with open (book) as f:
        book_content = f.read()
    return book_content

def main():
    words_count = number_of_words(get_book_text("books/frankenstein.txt"))
    character_count = number_of_characters(get_book_text("books/frankenstein.txt"))
    print(f"{words_count} words found in the document")
    print(character_count)

main()