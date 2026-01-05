def get_book_text(path):
    contents = None
    with open(path) as f:
        contents = f.read()
    return contents

def main():
    print("            BOOKBOT - A Better Book Botter")

    if len(sys.argv) != 2:
        print("    Error: Wrong number of parameters!")
        print("    Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    print(f" -- Analyzing book at path {path}")
    book = get_book_text(path)

    print(" -- Word count")
    print(count_words(book))

    print(" -- Character count")
    sorted_count = sort_count_characters(count_characters(book))
    for i in range(0, len(sorted_count)):
        if sorted_count[i]["char"].isalpha():
            print(f"{sorted_count[i]["char"]}: {sorted_count[i]["num"]}")

    sys.exit(0)

#Run from  here
import sys
from stats import count_words, count_characters, sort_count_characters

main()