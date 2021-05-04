'''
'''
K = input()
x, y = (ord(K[0]) - 96), int(K[1])
count = 0

for i in range(1, 3):
    nx = i
    if(i == 1) :
        ny = 2
    if(i == 2):
        ny = 1
    for k in range(4):
        if(k%2 == 0):nx *= -1
        else: ny *= -1
        if x+nx > 1 and y+ny > 1: count+=1
print(count)