def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = text_count(text)
    final_dict = (get_dictionary(text))
    final_report(book_path, final_dict, num_words )

def get_book_text(x):
    with open(x) as f:
        return f.read()

def text_count(y):
    words = y.split()
    return len(words)

def get_dictionary(z):
    default_dict = {}
    lower = z.lower()
    for i in lower:
        if i.isalpha() == True:
            if i in default_dict:
                default_dict[i] += 1
            else:
                default_dict[i] = 1
    return sort_dictionary(default_dict)

def sort_dictionary(unsorted_dict):
    list = sorted(unsorted_dict.items(), key=lambda x:x[1], reverse=True)
    new_dict = dict(list)
    final_dict = [{k: v} for k,v in new_dict.items()]
    return final_dict

def final_report(a, b, c, ):
    print(f"""-------- Report of {a}--------
          """)
    for i in b:
        for x in i:
            print(f"The {x} character was found in the book {i[x]} times.")
    print(f"""
The total number of words in this book is {c}
""")
    print("----------------- End Of Report -----------------")   


main()