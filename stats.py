
def count_words(path):
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        return word_count
    




def count_letters(words):
    with open(words) as input:
        file_contents = input.read()
    word = file_contents.lower()
    letters = word.split()
    #print(letters)
    sorted_letters = {}
    each_letters = list(word)
    #print(each_letters)
    for each_letter in each_letters:
        if each_letter in sorted_letters:
            sorted_letters[each_letter] += 1
        else:
            sorted_letters[each_letter] = 1
    print(sorted_letters)




