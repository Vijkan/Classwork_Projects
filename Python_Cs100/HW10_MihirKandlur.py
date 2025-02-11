'''
Mihir Kandlur
CS 100 Section 101 
HW 10, November 8, 2023
'''

def initialLetterCount(wordList):
    words = {}
    for word in wordList:
        word=word[0]
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1  

    return words

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetterCount(horton))

#Question 2
def initialLetters(wordList):
    words = {}
    for word in wordList:
        wordL=word[0]
        if wordL not in words:
            words[wordL] = word 

    return words    
print(initialLetters(horton))

#3
def shareOneLetter(wordList):
    words = {}

    for word in wordList:
        if word not in words:
            x = []
            for other_word in wordList:
                for letter in word:
                    if letter in other_word and other_word not in x:
                            x.append(other_word)
            words[word] = x
    
    return words


print(shareOneLetter(horton))



'''
{'I': 4, 's': 2, 'w': 2, 'm': 2, 'a': 1}
{'I': 'I', 's': 'say', 'w': 'what', 'm': 'mean', 'a': 'and'}
{'I': ['I'], 'say': ['say', 'what', 'mean', 'and'], 'what': ['say', 'what', 'mean', 'and'], 'mean': ['say', 'what', 'mean', 'and'], 'and': ['say', 'what', 'mean', 'and']}
'''



