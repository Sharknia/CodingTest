d = [[0 for j in range(20)] for i in range(20)] 

for i in range(19):
    x = input().split()
    for j in range(19):
        d[i][j] = x[j]
    
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for i in range(19):
        if d[x-1][i] == '0':
            d[x-1][i] = '1'
        else :
            d[x-1][i] = '0'
    for i in range(19):
        if d[i][y-1] == '0':
            d[i][y-1] = '1'
        else :
            d[i][y-1] = '0'

for i in range(19) : 
    for j in range(19) :  
        print(d[i][j], end=' ')
    print()