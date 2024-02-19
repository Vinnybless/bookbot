def book():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        return file_contents
    
    
def word_count():
    words = len(book().split())
    return f"Word Count: {words}"


def letter_count():
    letters = len(book())
    return f"Letter Count: {letters}"


def letters_dict():
    letters_and_count = {}
    all_letters = book().lower()
    for letter in all_letters:
        if letter.isalpha():
            if letter in letters_and_count:
                letters_and_count[letter] += 1
            else:
                letters_and_count[letter] = 1
    return letters_and_count


def on_sort(dict):
    return list(dict.values())[0]


def sort_that_shit():
    list_of_dicts = []
    for k, v in letters_dict().items():
        small_dict = {k: v}
        list_of_dicts.append(small_dict)
    list_of_dicts.sort(reverse=True, key=on_sort)
    for i in list_of_dicts:
        for k, v in i.items():
            print(f"The {k} letter appeared {v} times")


def main():
    print('==== Report ====')
    print(word_count())
    print(letter_count())
    sort_that_shit()


main()
