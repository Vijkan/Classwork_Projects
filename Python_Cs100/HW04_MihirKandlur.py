'''
Mihir Kandlur
CS 100 Section 101 
HW 04, OCtober 3, 2023
'''
from turtle import *
import turtle as t
#Question 1 & 2
#a
a=3
b=4
c=5
#b
if a<b:
    print('OK')
 
else:
     print('NOT OK')

#c
if c<b:
     print('OK')
else:
     print('NOT OK')
#d
if b==c:
     print('OK')
else:
     print('NOT OK')
#e
if ((b*b)==(c*c)):
     print('OK')
else:
     print('NOT OK')

#3 ask user for input color width lenght shp

def draw(col,wid,len,shp):
     t.down
     t.color(col)
     t.width(wid)
     shp=shp.lower()
     if shp=="line":
          shp=1
     if shp=="triangle":
          shp=3
     if shp=="square":
          shp=4
     for i in range(0,shp):
          t.forward(len) 
          t.left(360/shp)
     t.mainloop()

col=input("What color? ")
wid=int(input("Line width?"))
len=int(input("Line length?"))
shp=input("line, triangle or square?")
draw(col,wid,len,shp)
'''Output
OK
NOT OK
NOT OK
NOT OK
What color? red
Line width?25
Line length?100
line, triangle or square?LiNE
'''
