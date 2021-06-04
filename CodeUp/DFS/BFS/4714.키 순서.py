'''
1. 작은사람만 탐색한다. (배열 역방향)
2. 큰사람만 탐색한다. (배열 정방향)
3. 모두 방문했다면 이 학생의 순위를 알 수 있는 것. 

시간초과
'''
from collections import deque
from typing import Counter

###입력 받기 시작
tmp = input()
if(tmp.__len__() == 1) : 
    N = int(tmp)
    M = int(input())
else:
    N, M = map(int, tmp.split())

l = []  #비교 리스트
memoryP = [] #학생 위치 기록
memoryM = [] #학생 위치 기록
for i in range(N):
    memoryP.append([])
    memoryM.append([])
cnt = 0
for i in range(M):
    tmp = list(map(int, input().split()))
    memoryP[tmp[0] - 1].append(cnt)
    memoryM[tmp[1] - 1].append(cnt)
    l.append(tmp)
    cnt += 1
result = 0  #출력할 결과값
v = [False] * N #방문 여부
###입력 받기 종료

## 방문 여부 초기화
def resetVisited(v):
    v = [False] * N
    return v

## 전부 다 방문했는지 확인
def chkVisited(v):
    isVAll = True
    for i in v:
        if not i : isVAll = False
    return isVAll

for s in range(N):
    q = deque()
    
    q.append([s, 1])
    q.append([s, -1])

    while(q):
        tmp = q.popleft()
        nowStu = tmp[0] + 1
        d = tmp[1]
        v[nowStu - 1] = True

        if d > 0:
            for j in memoryP[nowStu - 1]:
                i = l[j]
                if i[0] == nowStu and not v[i[1] -1]:
                    q.append([i[1] - 1, d])
                    v[i[1] - 1] = True

        elif d < 0:
            for j in memoryM[nowStu - 1]:
                i = l[j]
                if i[1] == nowStu and not v[i[0] - 1]:
                    q.append([i[0] - 1, d])
                    v[i[0] - 1] = True

    if chkVisited(v) :  result += 1
    v = resetVisited(v)

print(result)