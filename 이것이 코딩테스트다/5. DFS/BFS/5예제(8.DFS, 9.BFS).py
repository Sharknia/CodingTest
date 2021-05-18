from collections import deque


graph = [
    [],
    [2, 3, 8],
    [1,7],
    [1,4,5],
    [4,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
### DFS 구현
visited = [False] * 9

def DFS(v):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        try:
            if not visited[i]:
                DFS(i)
        except:
            break

DFS(1)
### DFS 끝
print()
### BFS 구현
visited = [False] * 9

def BFS(v):
    q = deque()
    q.append(v)
    #현재 노드 방문 처리
    visited[v] = True
    #queue가 빌 때 까지 반복
    while q:
        v = q.popleft()
        print(v, end=' ')
        #해당 원소와 연결된 방문하지 않은 원소들 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i]=True
    
BFS(1)
### BFS 끝