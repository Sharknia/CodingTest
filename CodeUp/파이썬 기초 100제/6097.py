h, w = map(int, input().split()) #격자판 세로 h, 격자판 가로 w

target = [[0 for i in range(w)] for i in range(h)]

n = int(input())    #막대 개수 n
for i in range(n):
    l, d, x, y = map(int, input().split())  #막대 길이 l, 방향 d(가로 0 세로 1), 좌표 x, y
    x -= 1
    y -= 1
    for j in range(l):
        #가로의 경우
        if d == 0:
            target[x][y + j] = 1
        #세로의 경우
        else :
            target[x + j][y] = 1
            

for i in range(h) : 
    for j in range(w) :  
        print(target[i][j], end=' ')
    print()