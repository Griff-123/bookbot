def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = text_count(text)
    final_dict = (get_dictionary(text))
    print(f"""-------- Report of {book_path}--------
          """)
    for i in final_dict:
        for x in i:
            print(f"The {x} character was found in the book {i[x]} times.")
    print(f"""
The total number of words in this book is {num_words}
""")
    print("----------------- End Of Report -----------------")

def get_dictionary(z):
    default_dict = {}
    lower = z.lower()
    for i in lower:
        if i.isalpha() == True:
            if i in default_dict:
                default_dict[i] += 1
            else:
                default_dict[i] = 1
    new_dict = sorted(default_dict.items(), key=lambda x:x[1], reverse=True)
    set_list = dict(new_dict)
    new_list = [{k: v} for k,v in set_list.items()]
    
    return new_list


def text_count(y):
    words = y.split()
    return len(words)

def get_book_text(x):
    with open(x) as f:
        return f.read()

    



main()