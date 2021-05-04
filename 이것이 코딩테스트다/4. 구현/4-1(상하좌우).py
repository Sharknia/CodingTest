'''
'''

N = int(input()) #정사각형의 크기
L = input().split()
x = 1
y = 1
for i in L:
    if(i == 'R'):
        y=y+1
    elif(i=='L'):
        y=y-1
    elif(i=='U'):
        x=x-1
    elif(i=='D'):
        x=x+1
    
    if(y < 1): y = 1
    if(x < 1): x = 1
    if(y > N): y = N
    if(x > N): x = N

print(x, y)
