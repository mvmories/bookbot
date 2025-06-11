def get_num_words(book_text):
    return len(book_text.split())

def get_chars_dict(book_text):
    char_dict = {}
    for char in book_text:
        lower_char = char.lower()
        if lower_char in char_dict:
            char_dict[lower_char] += 1
        else:
            char_dict[lower_char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_char_dict):
    sorted_list = []
    for char in num_char_dict:
        count = num_char_dict[char]
        dict = {"char": char, "num": count}
        sorted_list.append(dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list