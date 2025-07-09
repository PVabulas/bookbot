
import sys
from stats import get_num_words, get_char_counts, sort_dict

def get_book_test(path_to_file: str):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file = sys.argv[1]
    t = get_book_test(file)
    n = get_num_words(t)
    c = get_char_counts(t)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {n} total words")
    print("--------- Character Count -------")
    for d in sort_dict(c):
        print(f"{d["char"]}: {d["num"]}")

main()