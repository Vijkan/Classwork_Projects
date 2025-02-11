'''''
Mihir Kandlur
CS 100 Section 101 
HW 07, October 25, 2023
'''
# The Bells
# Edgar Allen Poe
theBells = '''
HEAR the sledges with the bells,
Silver bells!
What a world of merriment their melody foretells!
How they tinkle, tinkle, tinkle,
In the icy air of night!
While the stars, that oversprinkle
All the heavens, seem to twinkle
With a crystalline delight;
Keeping time, time, time,
In a sort of Runic rhyme,
To the tintinnabulation that so musically wells
From the bells, bells, bells, bells,
Bells, bells, bells--
From the jingling and the tinkling of the bells.
Hear the mellow wedding bells,
Golden bells!
What a world of happiness their harmony foretells!
Through the balmy air of night
How they ring out their delight!
From the molten-golden notes,
And all in tune,
What a liquid ditty floats
To the turtle-dove that listens, while she gloats
On the moon!
Oh, from out the sounding cells,
What a gush of euphony voluminously wells!
How it swells!
How it dwells
On the Future! how it tells
Of the rapture that impels
To the swinging and the ringing
Of the bells, bells, bells,
Of the bells, bells, bells, bells,
Bells, bells, bells--
To the rhyming and the chiming of the bells!
Hear the loud alarum bells,
Brazen bells!
What a tale of terror, now, their turbulency tells!
In the startled ear of night
How they scream out their affright!
Too much horrified to speak,
They can only shriek, shriek,
Out of tune,
In a clamorous appealing to the mercy of the fire,
In a mad expostulation with the deaf and frantic fire,
Leaping higher, higher, higher,
With a desperate desire,
And a resolute endeavor
Now--now to sit or never,
By the side of the pale-faced moon.
Oh, the bells, bells, bells!
What a tale their terror tells
Of Despair!
How they clang, and clash, and roar!
What a horror they outpour
On the bosom of the palpitating air!
Yet the ear it fully knows,
By the twanging
And the clanging,
How the danger ebbs and flows;
Yet the ear distinctly tells,
In the jangling
And the wrangling,
How the danger sinks and swells,--
By the sinking or the swelling in the anger of the bells,
Of the bells,
Of the bells, bells, bells, bells,
Bells, bells, bells--
In the clamor and the clangor of the bells!
Hear the tolling of the bells,
Iron bells!
What a world of solemn thought their monody compels!
In the silence of the night
How we shiver with affright
At the melancholy menace of their tone!
For every sound that floats
From the rust within their throats
Is a groan.
And the people--ah, the people,
They that dwell up in the steeple,
All alone,
And who tolling, tolling, tolling,
In that muffled monotone,
Feel a glory in so rolling
On the human heart a stone--
They are neither man nor woman,
They are neither brute nor human,
They are Ghouls:
And their king it is who tolls;
And he rolls, rolls, rolls,
Rolls
A paean from the bells;
And his merry bosom swells
With the paean of the bells,
And he dances, and he yells:
Keeping time, time, time,
In a sort of Runic rhyme,
To the paean of the bells,
Of the bells:
Keeping time, time, time,
In a sort of Runic rhyme,
To the throbbing of the bells,
Of the bells, bells, bells--
To the sobbing of the bells;
Keeping time, time, time,
As he knells, knells, knells,
In a happy Runic rhyme,
To the rolling of the bells,
Of the bells, bells, bells:
To the tolling of the bells,
Of the bells, bells, bells, bells,
Bells, bells, bells--
To the moaning and the groaning of the bells.
'''
# Canto XII from The Heights of Macchu Picchu
# Pablo Neruda
cantoXII = '''
Arise to birth with me, my brother.
Give me your hand out of the depths
sown by your sorrows.
You will not return from these stone fastnesses.
You will not emerge from subterranean time.
Your rasping voice will not come back,
nor your pierced eyes rise from their sockets.
Look at me from the depths of the earth,
tiller of fields, weaver, reticent shepherd,
groom of totemic guanacos,
mason high on your treacherous scaffolding,
iceman of Andean tears,
jeweler with crushed fingers,
farmer anxious among his seedlings,
potter wasted among his clays--
bring to the cup of this new life
your ancient buried sorrows.
Show me your blood and your furrow;
say to me: here I was scourged
because a gem was dull or because the earth
failed to give up in time its tithe of corn or stone.
Point out to me the rock on which you stumbled,
the wood they used to crucify your body.
Strike the old flints
to kindle ancient lamps, light up the whips
glued to your wounds throughout the centuries
and light the axes gleaming with your blood.
I come to speak for your dead mouths.
Throughout the earth
let dead lips congregate,
out of the depths spin this long night to me
as if I rode at anchor here with you.
And tell me everything, tell chain by chain,
and link by link, and step by step;
sharpen the knives you kept hidden away,
thrust them into my breast, into my hands,
like a torrent of sunbursts,
an Amazon of buried jaguars,
and leave me cry: hours, days and years,
blind ages, stellar centuries.
And give me silence, give me water, hope.
Give me the struggle, the iron, the volcanoes.
Let bodies cling like magnets to my body.
Come quickly to my veins and to my mouth.
Speak through my speech, and through my blood.
'''
import string
def litCricFriend(wordList, text):
    lenth=len(text)
    wordList=[word.lower() for word in wordList]
    count=0
    text=text.lower()
    text.replace('--',' ' )
    text=text.split()
    lst=[]

    for word in text: 
        lst.append(word.strip(string.punctuation))

    for i in range(0,len(lst)):
        if lst[i] in wordList:
            count+=1

    rat=count/lenth
    return(rat)
    
    
'''
computing and returning the frequency with which specified words
(wordList) appear in a body of text (text). Frequency is
the sum of the number of times that each word in wordList
occurs, divided by the number of words in the text. A word
occurrence is the whole word, regardless of case, and
excluding punctuation. 
'''
# PROBLEM 1. Write a string method call that lower cases all
# of the characters in text. One line of code. Hint: assign the
# lower-cased text to a new variable name.
lowbell=theBells.lower()
# PROBLEM 2. Write a string method call that replaces every
# m-dash ('--') in the lower-cased text with a space (' ').
# One line of code.
lowbell=lowbell.replace('--',' ' )
# PROBLEM 3. Write a string method call that splits text into a
# list of words (after they have been lower-cased, and the
# m-dashes removed). One line of code.
lowbell=lowbell.split()
# PROBLEM 4. Write a loop that creates a new word list, using a
# string method to strip the words from the list created in Problem 3
# of all leading and trailing punctuation. Hint: the string library,
# which is imported above, contains a constant named punctuation.
# Three lines of code.
lst=[]
for word in lowbell: 
    lst.append(word.strip(string.punctuation))


# PROBLEM 5. Write a loop that sums the number of times that the
# words in wordList occur in the list from Problem 4. Hint 1: you
# can use a list method to do the counting. Hint 2: lower case the
# words in wordList. Between three and five lines of code. (It
# depends on your coding style -- various styles are OK.)
wordList=["bells","GHouls"]
count=0

for i in range(0,len(lst)):
        if lst[i] in [word.lower() for word in wordList]:
            count+=1

# PROBLEM 6. Calculate the ratio of the number from Problem 5
# to the number of words in text. Return this ratio. Between one
# and three lines of code. (It depends on your coding style --
# various styles are OK.)
ratio=count/len(theBells)
# PROBLEM 7. Call litCricFriend() four times to find the frequency
# of the indefinite articles 'a' and 'an' and the definite article
# 'the' in the two poems above. Print out the value returned by
# each function call, identifying what it is. For example, it might say
# >>> bellsAAnFrequency 0.07265587064676617.
# (That is a made-up number.) Each function call takes one line.
p71=litCricFriend(["a","an"],theBells)
p72=litCricFriend(["a","an"],cantoXII)
p73=litCricFriend(["the"],theBells)
p74=litCricFriend(["the"],cantoXII)
print("The frequency at which poe uses a , an is", p71, "the frequency at which Nerunda used it is" , p72)
print("The frequency at which poe uses the is", p73, "the frequency at which Nerunda used it is" , p74)
# PROBLEM 8. Do the results show that Poe and Neruda use 'a' and 'an'
# differently? Do the results show that Poe and Neruda use 'the'
# differently?

'''
Yes it does poe uses a and an much more frequently then Neruda about 5 times as often
while pow uses the about twice as often

'''
'''
The frequency at which poe uses a , an is 0.006323396567299007 the frequency at which Nerunda used it is 0.0017543859649122807
The frequency at which poe uses the is 0.024691358024691357 the frequency at which Nerunda used it is 0.009941520467836258
'''
