from collections import deque

'''
디큐를 써보겠습니다.
리스트로 주어지는군여
방문여부 체크하는 지도와 숫자 카운팅하는 지도

좀 이쁘게 다시 짜보자
'''
g1 = [] #방문여부 체크, 방문했으면 1
g2 = [] #카운트

t = []

n = int(input())    #컴퓨터의 개수
for i in range(n):
    g1.append(0)
    g2.append(0)

m = int(input())    #쌍의 개수

for i in range(m):
    x, y = list(map(int, input().split()))
    t.append([x, y])

q = deque()
q.append(1)

while(q):
    x = q.popleft()
    g1[x - 1] = 1
    for i in t:
        try:
            v = i.index(x)
            if v == 1 : v = 0
            else : v = 1
            if g1[i[v] - 1] == 0 : q.append(i[v])
            if g2[i[v] - 1] == 0 : g2[i[v] - 1] = max(g2) + 1
        except:
            continue
print(max(g2) - 1)