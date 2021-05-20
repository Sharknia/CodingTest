'''
전광판 전구조작
켤 떄 최소횟수, 킬 때 최소 횟수!
아이스크림이나 애니팡이랑 비슷한 문제로 보인다!
'''

n, m = map(int, input().split()) 
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


def DFS(x, y, onoff):
    #범위를 벗어나면 바로 종료
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    #해당칸이 동작해야하는(꺼야 하거나 켜야 하거나)상황과 같다면 바로 종료
    if tempMap[x][y] == onoff or tempMap[x][y] == 9:
        return False
    #해당칸이 지도 안에 있고, 켜야 하거나 꺼야 하는 칸이라면 해당 칸 키거나 끄고 주변칸 호출
    tempMap[x][y] = 9
    DFS(x-1, y, onoff)
    DFS(x, y-1, onoff)
    DFS(x+1, y, onoff)
    DFS(x, y+1, onoff)

    return True

result0 = 0
result1 = 0

for onoff in range(2):
    tempMap = graph

    for i in range(n):
        for j in range(m):
            if (DFS(i, j, onoff)):
                if onoff == 0 : result0 += 1
                elif onoff == 1 : result1 += 1

print(result1, result0)