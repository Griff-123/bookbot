def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = text_count(text)
    print(get_dictionary(text))

def get_dictionary(z):
    default_dict = {}
    lower = z.lower()
    for i in lower:
        if i in default_dict:
            default_dict[i] += 1
        else:
            default_dict[i] = 1
    return default_dict


def text_count(y):
    words = y.split()
    return len(words)

def get_book_text(x):
    with open(x) as f:
        return f.read()


main()