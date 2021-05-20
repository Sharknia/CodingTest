###
# 캔디팡 문제
# 같은 덩어리를 찾는 문제로, 내 가설에 따라 전부 다 확인해야 하므로 DFS로 보인다. 
# 따라서 재귀함수를 이용한 문제 풀이를 하겠습니다.
# 음료수 얼려먹기의 확장판. 못하면 나가죽자
###

n = 7 
m = 7
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


'''
1. 색깔 정보가 1~5까지이므로 이미 방문한곳은 0으로 하기로 한다. 
2. 이미 방문한 곳이라면 다음칸으로 넘어간다. 
3. 방문한 곳이 아니라면 해당칸을 방문처리한다. 
4. 다른 숫자거나, 범위가 아니라면 return False 한다. (방문처리하지 않는다.)
'''

bomb = 0

def DFS(x, y, color, result):
    # print(x, y, color, result)
    if x < 0 or x >= n or y < 0 or y >= m:
        return 0
    if graph[x][y] != color or graph[x][y] == 0:
        return 0
    #방문처리
    if graph[x][y] != 0:
        graph[x][y] = 0
        result += DFS(x-1, y, color, result)
        result += DFS(x, y-1, color, result)
        result += DFS(x+1, y, color, result)
        result += DFS(x, y+1, color, result)
        return result
    else:
        return 0

for i in range(n):
    for j in range(m):
            if DFS(i, j, graph[i][j], 1) > 2 : 
                bomb+=1

print(bomb)