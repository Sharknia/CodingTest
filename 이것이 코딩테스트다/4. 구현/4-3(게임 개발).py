'''
'''

x, y = map(int, input().split())
dy, dx, dr = map(int, input().split())  #x좌표, y좌표, 보고 있는 방향 (북0 동1 남2 서3)

count = 1 #밟은 땅 수

h = [[0 for j in range(x)] for i in range(y)] #이동한 history
m = [[0 for j in range(x)] for i in range(y)] #지도
h[dx][dy] = 1
print(h)
for i in range(x):
    a = input().split()
    for j in range(y):
        m[i][j] = int(a[j])

while(True):
    #보고 있는 방향이 0이라면 이동한다. (이동 카운트 +1)
    #보고 있는 방향이 1이라면 좌회전한다. 
    #더 이상 이동할 수 없다면 한 칸 뒤로 간다. (제자리로 돌아온 후 보고 있는 방향으 h가 1이라면 내가 왔던 방향)
    break

print(count)