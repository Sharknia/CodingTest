n, m = map(int, input().split()) 
##지도 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def DFS(x, y):
    #주어진 범위를 벗어나면(벽에 닿거나 지도 바깥이라면) 즉시 종료
    if x<= -1 or x >= n or y <= -1 or y >= m:
        print(x, y)
        return False
    
    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        #해당 노드 방문처리
        graph[x][y] = 1
        ##모든 근접 재귀호출
        DFS(x-1, y)
        DFS(x, y-1)
        DFS(x+1, y)
        DFS(x, y+1)
        return True
    #노드를 방문했다면 False값을 반환한다.
    else :
        return False

##호출 시작
result = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 DFS 수행
        if DFS(i, j):
            result +=1

print(result)
    