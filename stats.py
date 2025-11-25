
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
    return word_count
