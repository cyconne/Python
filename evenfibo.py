#num 7

x,y = 1, 1
total=0
while x<=4000000:
    if x % 2 == 0:
        total +=x
    x, y = y, x+y
print (total)
