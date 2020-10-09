import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

words_file = open(os.path.join(__location__, 'words.txt'))
book_file = open(os.path.join(__location__, 'The Time Machine by H. G. Wells.txt'))

words = {}

for line in words_file:
    for word in line.split():
        words[word.lower()] = 1

print('done')

incorrect_words = []
punctuation = ['.', ',', '!', '"', '\'', '?', ':', ';','...']

def checkWord(word):
    if (word[-1:] in punctuation):
        word = word[:-1]
    if (len(word) > 1):
        if (word[0] == '"'):
            word = word [1:]
    if (word[-2:] == '\'s'):
        word = word[:-2]
    if ('--' in word):
        for newWord in word.split('--'):
            checkWord(newWord)
        return
    if ('-' in word):
        for newWord in word.split('-'):
            checkWord(newWord)
        return

    if (words.get(word.lower()) == None and word != ''):
        incorrect_words.append(word)

for line in book_file:
    for word in line.split():
        checkWord(word)


print(incorrect_words)
