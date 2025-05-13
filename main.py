from stats import number_of_words, number_of_characters, character_count_sorted
import sys

# Reads a file and returns the text as a string
def get_book_text(book):
    with open (book) as f:
        book_content = f.read()
    return book_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_content = get_book_text(sys.argv[1])
    word_count = number_of_words(book_content)
    character_count = number_of_characters(book_content)
    sorted_count = character_count_sorted(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_count:
        if item["char"].isalpha() == True:
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()