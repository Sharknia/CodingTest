

d = [[0 for j in range(10)] for i in range(10)] 
for i in range(10):
    a = input().split()
    for j in range(10):
        d[i][j] = int(a[j])

x = 1
y = 1

while True:
    if d[x][y] == 2 :
        d[x][y] = 9
        break
    #오른쪽이 0이라면 이동한다.
    #오른쪽이 0이 아니고 아래가 0이라면 이동한다 .
    #둘 다 아니라면 멈춘다.
    if y < 8 and (d[x][y+1] == 0 or d[x][y+1] == 2):
        d[x][y] = 9
        y += 1
    elif x < 8 and (d[x+1][y] == 0 or d[x+1][y] == 2):
        d[x][y] = 9
        x += 1
    else:
        d[x][y] = 9
        break

for i in range(10) : 
    for j in range(10) :  
        print(d[i][j], end=' ')
    print()