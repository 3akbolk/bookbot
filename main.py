from stats import count_letters
from stats import count_words
import sys


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


seperated_words = {}
def test1():
    word_count = count_words(sys.argv[1])
    print(f"Found {word_count} total words.")
    
    
def test2():
    words = (sys.argv[1])
    seperated_words = count_letters(words)
    for char in seperated_words:
        print(char)


print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
test1()
print("--------- Character Count -------")
test2()
print("============= END ===============")

