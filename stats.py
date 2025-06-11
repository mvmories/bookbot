def get_num_words(book_text):
    return len(book_text.split())

def get_num_chars(book_text):
    char_dict = {}
    for char in book_text:
        lower_char = char.lower()
        if lower_char in char_dict:
            char_dict[lower_char] += 1
        else:
            char_dict[lower_char] = 1
    return char_dict