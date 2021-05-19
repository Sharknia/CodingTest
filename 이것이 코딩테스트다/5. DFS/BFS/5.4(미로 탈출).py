# n, m = map(int, input().split()) 
# ##지도 입력
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

###최단거리는 BFS구나 내가 한심하다

from collections import deque

###테스트 값
n = 5
m = 6
graph=[
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
]


dx=[-1, 1, 0, 0]
dy=[0 ,0 ,-1 ,1]

def BFS(x, y):
    #큐 구현을 위한 라이브러리 사용
    queue = deque()
    queue.append((x, y))

    #큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #미로찾기 범위가 아니면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            #벽인 경우 무시
            if graph[nx][ny] == 0 :
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]

print(BFS(0, 0))
        
