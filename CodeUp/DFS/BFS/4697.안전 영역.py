'''
DFS면 100x100 사이즈에서 스택 오버플로우
'''
from collections import deque

graph = []
a = 9999
b = -1
N = int(input())
for i in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    if min(tmp) < a : a = min(tmp)
    if max(tmp) > b : b = max(tmp)

dx=[-1, 1, 0, 0]
dy=[0 ,0 ,-1 ,1]

# N = 100
# graph = []
# test = 1
# for i in range(100):
#     tmp = []
#     for j in range(100):
#         tmp.append(test)
#         test += 1
#         if test > 97 : test = 1
#     graph.append(tmp)
a = 1
b = 98

visited = []
result = 1

#방문 리셋
def resetVisted(visited):
    visited = []
    for i in range(N):
        visited.append([0]*N)
    return visited
    
def DFS(h, graph, visited, x, y):
    try:
        #칸을 벗어났다면 return
        if x < 0 or x >= N or y < 0 or y >= N : return 0 
        #이미 방문했다면 return
        if visited[x][y] == 1 : return 0
        #방문 가능하고 첫 방문이므로 방문처리
        visited[x][y] = 1
        #높이보다 낮거나 같다면 return
        if graph[x][y] <= h : return 0
        #방문한 곳이 아니고, 높이보다 높다면 안전지대이다. 
        #해당 위치를 방문처리하고 주변을 탐색한다. 
        # print(x, y, graph[x][y])
        DFS(h, graph, visited, x+1, y)
        DFS(h, graph, visited, x, y+1)
        DFS(h, graph, visited, x-1, y)
        DFS(h, graph, visited, x, y-1)
        return 1
    except:
        return 0

def BFS(h, graph, visited, x, y):
    result = 0
    #이미 방문했다면 return
    if visited[x][y] == 1 : return 0
    if graph[x][y] <= h : return 0
    #방문처리
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while(q):
        x, y = q.popleft()
        # print(x,y)
        visited[x][y] = 1
        result = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #칸을 벗어났다면
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            #잠기는 경우 무시
            if graph[nx][ny] <= h :
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))
            else : continue
    return result

for i in range(a, b):
    # print("[[[[[[[[[[[[[["+str(i)+"]]]]]]]]]]]]]]]")
    tmpRes = 0
    visited = resetVisted(visited)
    for x in range(N):
        for y in range(N):
            tmpRes += BFS(i, graph, visited, x, y)
    # print(i, tmpRes)
    if result < tmpRes: 
        result = tmpRes
    
# tmpRes = 0
# visited = resetVisted(visited)
# for x in range(N):
#     for y in range(N):
#         tmpRes += BFS(95, graph, visited, x, y)
    
if result < tmpRes: result = tmpRes
print(result)