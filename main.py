from stats import get_book_text

def main():
    word_count = get_book_text("/home/zakbolk/workspace/bookbot/books/frankenstein.txt")
    print(f"Found {word_count} total words.")


main()

