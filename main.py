from stats import number_of_words

# Reads a file and returns the text as a string
def get_book_text(book):
    with open (book) as f:
        book_content = f.read()
    return book_content

# Calls get_book_text and number_of_words to get the number of words in the frankenstein text
def main():
    words_count = number_of_words(get_book_text("books/frankenstein.txt"))
    print(f"{words_count} words found in the document")


main()