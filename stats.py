
def count_words(path):
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        return word_count
    


dictionary = {}

def count_letters(words):
    with open(words) as input:
        file_contents = input.read()
    word = file_contents.lower()
    #do I need this line?? vvvv
    letters = word.split()
    #reads and splits the words in frankenstein
    sorted_letters = {}
    each_letters = list(word)
    #sorts and adds to sorted_letters dictionary
    for each_letter in each_letters:
        if each_letter in sorted_letters:
            sorted_letters[each_letter] += 1
        else:
            sorted_letters[each_letter] = 1
    #return (sorted_letters)

    
    
    for character, value in sorted_letters.items():
        dictionary[character] = value
    return (dictionary)







