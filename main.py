# open the file at this path, assign the contents to a variable, return variable, close file
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

# assign the book contents (string) to a variable that can be passed to other functions
frankenstein = main()

# count the number of words in the passed book
def count_words(book):  
    counter = 0
    word_list = book.split()
    for i in word_list:
        counter += 1
    print (f"This book contains {counter} words!")

# convert book to lowercase, then increment letters in dictionary every time we see it in the book.
# print the dictionary after counting all letters
def char_count(book):
    lowercase_book = book.lower()
    letter_dict = { "a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0, "h" : 0, "i" : 0, "j" : 0,
                   "k" : 0, "l" : 0, "m" : 0, "n" : 0, "o" : 0, "p" : 0, "q" : 0, "r" : 0, "s" : 0, "t" : 0,
                   "u" : 0, "v" : 0, "w" : 0, "x" : 0, "y" : 0, "z" : 0 }
    for i in lowercase_book:
        if i in letter_dict:
            letter_dict[i] += 1
    return letter_dict

# assign the character count function's return to a variable to be used in the report function later
letter_count = char_count(frankenstein)

# dilineates the start and end of the book report, and prints the number of words and
# letter counts on individual lines
def report(book,letter_count):
    print ("--- Begin report of frankenstein.txt ---")
    count_words(book)

    for key in letter_count:
        print (f"The letter '{key}' appears {letter_count[key]} times!")

    print ("--- End report ---")

# call the report function to begin the book report
report(frankenstein, letter_count)