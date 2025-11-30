from stats import count_letters
from stats import count_words


seperated_words = {}
def test1():
    word_count = count_words("/home/zakbolk/workspace/bookbot/books/frankenstein.txt")
    print(f"Found {word_count} total words.")
    
    

    
def test2():
    words = ("/home/zakbolk/workspace/bookbot/books/frankenstein.txt")
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

