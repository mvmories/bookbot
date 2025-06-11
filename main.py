from stats import get_num_words, get_num_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text("./books/frankenstein.txt")

    # Count total words in book
    num_word = get_num_words(book_text)
    word_count = f"{num_word} words found in the document"

    # Count chars in book
    char_count = get_num_chars(book_text)

    print(word_count)
    print(char_count)

main()