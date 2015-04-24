import math

x = 2.0 
y = 5.0 

a = 50
b = 50

c = x - a
d = y - b

e = c*c
f = d*d


e = math.sqrt(e)
f = math.sqrt(f)


if e > f:
    print('wohoo')

if type(e) is int:
    print('WHY IS THIS AN INT?')

if type(e) is float:
    print('WHY DO YOU NOT WORK THEN?!!?!?!')
