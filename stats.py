
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
    #reads and splits the words in frankenstein
    sorted_letters = {}
    letters = list(word)
    #sorts and adds to sorted_letters dictionary
    for letter in letters:
        if letter in sorted_letters:
            sorted_letters[letter] += 1
        else:
            sorted_letters[letter] = 1
    
    results = []
    def sort_by(items):
        return items["num"]
    for letter, number in sorted_letters.items():
        results.append({"character":letter, "num":number})
    
    results.sort(reverse=True, key=sort_by)
    finals = []
    for result in results:
        if not result["character"].isalpha():
            continue
        else:
            finals.append(f"{result['character']}: {result['num']}")
    #for final in finals:
    return(finals)
    


    






