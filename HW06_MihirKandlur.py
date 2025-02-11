'''
Mihir Kandlur
CS 100 Section 101 
HW 06, October 17, 2023
'''
#Question 1
def hasFinalLetter (strLists,letters):
    finaleList=list()
    for i in range(0,len(strLists)):
        if strLists[i][-1]==letters:
               finaleList.append(strLists[i])
    return(finaleList)

lst=['jake','ending','house','protracter','compute']

x=hasFinalLetter(lst,'e')
print(x)

# Question 1 B

# Test case 1
strLists1 = ["apple", "banana", "orange", "pineapple", "bed"]
letters1 = "a"
result1 = hasFinalLetter(strLists1, letters1)
print(f"Test 1: {result1}") 

# Test case 2
strLists2 = ["dog", "bod", "log", "smog"]
letters2 = "g"
result2 = hasFinalLetter(strLists2, letters2)
print(f"Test 2: {result2}") 

# Test case 3
strLists3 = ["zebra", "lebra", "pig", "midterm", "sprite"]
letters3 = "z"
result3 = hasFinalLetter(strLists3, letters3)
print(f"Test 3: {result3}")  


# Question 2

def isDivisible(maxInt,twoInts):
    lst=[]
    for i in range(1,maxInt):
            if i%twoInts[0]==0 and i%twoInts[1]==0:
                  lst.append(i)
    return(lst)

#Question 2 B
    
# Test Case 1
maxInt1 = 20
twoInts1 = (2, 3)
result1 = isDivisible(maxInt1, twoInts1)
print(f"Test 1: {result1}")  

# Test case 2
maxInt2 = 15
twoInts2 = (4, 7)
result2 = isDivisible(maxInt2, twoInts2)
print(f"Test 2: {result2}")  

# Test case 3
maxInt3 = 30
twoInts3 = (3, 5)
result3 = isDivisible(maxInt3, twoInts3)
print(f"Test 3: {result3}")   


'''' Output

['jake', 'house', 'compute']
Test 1: ['banana']
Test 2: ['dog', 'log', 'smog']
Test 3: []
Test 1: [6, 12, 18]
Test 2: []
Test 3: [15]
'''