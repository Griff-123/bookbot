def main():
    book_path = "books/test.txt"
    text = get_book_text(book_path)
    dictt = {}
    for i in text:
        if i in dictt:
            dictt[i] += 1
        else:
            dictt[i] = 1
    print(dictt)



def get_book_text(x):
    with open(x) as f:
        return f.read()
    





main()