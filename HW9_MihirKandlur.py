'''
Mihir Kandlur
CS 100 Section 101 
HW 09, November 1, 2023
'''

# Question 1
def file_copy(in_file, out_file):
    out_file=open(out_file, 'w')
    in_file=open(in_file, 'r')
    
    out_file.write(in_file.read())
    in_file.close()
    out_file.close()

file_copy('created_equal.txt', 'copy.txt')


def file_stats(in_file):
    in_file = open(in_file, 'r')
    lines = 0
    words = 0
    characters = 0

    for line in in_file:
        lines += 1
        words += len(line.split())
        characters += len(line)

    print('lines', lines)
    print('words', words)
    print('characters', characters)

    in_file.close()

file_stats('created_equal.txt')

#Question 3
import string

def repeat_words(in_file, out_file):
    in_file = open(in_file, 'r')
    out_file = open(out_file, 'w')
    
    for line in in_file:
        repeated_words = set()
        words = line.lower().split()
        
        for word in words:
            cleaned_word = word.strip(string.punctuation)
            if cleaned_word in repeated_words:
                out_file.write(cleaned_word + ' ')
            repeated_words.add(cleaned_word)
        
        out_file.write('')
    
    in_file.close()
    out_file.close()

inF = 'catInTheHat.txt'
outF = 'catRepWords.txt'
repeat_words(inF, outF)

'''
lines 1     # the document said it was okay if we got 1 indstead of 2 
words 12
characters 76
'''




