def main():
    book_path = "books/test.txt"
    text = get_book_text(book_path)
    num_words = text_count(text)
    print(num_words)
    print(text)

def text_count(y):
    words = y.split()
    return len(words)

def get_book_text(x):
    with open(x) as f:
        return f.read()
    

main()