'''
Mihir Kandlur
CS 100 Section 101 
HW 08, October 25, 2023
'''
def twoWords(length,firstLetter):
    lst=[]
    while True:
        a1=input(("Enter a ",length," letter word"))
        if len(a1)==length:
            lst.append(a1)
            break
        else:
            continue

    while True:
        a2=input(("Enter a word that starts with",firstLetter))
        if a2[0].lower()==firstLetter.lower():
            lst.append(a2)
            break
        else:
            continue
    return(lst)

print(twoWords(3,"b"))

def twoWordsV2(lenght,firstLetter):
    lst=[]
    a1=input(("Enter a ",lenght," letter word"))
    while(len(a1)!=lenght):
        a1=input(("Enter a ",lenght," letter word"))
    lst.append(a1)
    a2=input(("Enter a word that starts with",firstLetter))
    while(a2[0].lower()!=firstLetter.lower()):
        a2=input(("Enter a word that starts with",firstLetter))
    lst.append(a2)
    return(lst)
print(twoWordsV2(3,"b"))

def enterNewPassword():
    num = '0123456789'
    
    while True:
        password = input("Enter a password that is between 8-15 characters and has at least 1 digit: ")
        
        if len(password) < 8 or len(password) > 15:
            print("Needs to be between 8 and 15 characters.")
        else:
            containsDigit = False
            for x in range(0, len(password)):
                if password[x] in num:
                    containsDigit = True
                    break
            
            if not containsDigit:
                print("Password must contain at least 1 digit.")
            else:
                break
enterNewPassword()



import random

def guessNumberGame():
    lowerBound = 0
    upperBound = 50
    numberToGuess = random.randint(lowerBound, upperBound)
    maxAttempts = 5
    attempts = 0

    print("I'm thinking of a number in the range", lowerBound, "-", upperBound, ". you have", maxAttempts, "tries to guess it.")

    while attempts < maxAttempts:
        attempts += 1
        userGuess = int(input("Guess " + str(attempts) + "? "))

        if userGuess < numberToGuess:
            print(str(userGuess) + " is too low")
        elif userGuess > numberToGuess:
            print(str(userGuess) + " is too high")
        else:
            print("you're right! I was thinking of", numberToGuess)
            return

    print("you've run out of attempts the correct number was", numberToGuess)

guessNumberGame()

'''
('Enter a ', 3, ' letter word')bog
('Enter a word that starts with', 'b')Bog
['bog', 'Bog']
('Enter a ', 3, ' letter word')Logger
('Enter a ', 3, ' letter word')Log
('Enter a word that starts with', 'b')Brock
['Log', 'Brock']
Enter a password that is between 8-15 characters and has at least 1 digit: pass
Needs to be between 8 and 15 characters.
Enter a password that is between 8-15 characters and has at least 1 digit: Password
Password must contain at least 1 digit.
Enter a password that is between 8-15 characters and has at least 1 digit: Password12
I'm thinking of a number in the range 0 - 50 . you have 5 tries to guess it.
Guess 1? 7
7 is too low
Guess 2? 14
14 is too low
Guess 3? 23
23 is too low
Guess 4? 45
45 is too high
Guess 5? 32
32 is too low
you've run out of attempts the correct number was 42
'''
