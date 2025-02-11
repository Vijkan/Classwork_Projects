'''
Mihir Kandlur
CS 100 Section 101 
HW 05, September 28, 2023
'''
#Question 1
months=["January","February","March","April","May","June","July","August","September","October","November","December"]

i=0
for i in range(0,len(months)):
    if "J" in months[i][0]:
        print(months[i])

#Question 2
for i in range(0,100):
    if (i%2==0) or (i%5==0):
        print(i)

#Question 3

horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"
x=0
for i in range(0,len(horton)):
    for x in range (0,len(vowels)):
        if horton[i]==vowels[x]:
            print(horton[i])


''' Output
January
June
July
0
2
4
5
6
8
10
12
14
15
16
18
20
22
24
25
26
28
30
32
34
35
36
38
40
42
44
45
46
48
50
52
54
55
56
58
60
62
64
65
66
68
70
72
74
75
76
78
80
82
84
85
86
88
90
92
94
95
96
98
A
e
o
a
e
o
o
a
e
o
a
''' 




