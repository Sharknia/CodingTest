'''
요약하자면 각 행의 가장 작은 숫자들 중 가장 큰 숫자를 고르라는 이야기다.
'''

'''
내 코드. 완벽했지만 min함수를 사용하는게 더 좋겠다!

#행의 개수 N, 열의 개수 M
N, M = map(int, input().split())

r = 0

for i in range(N):
    L = list(map(int, input().split()))
    L.sort(reverse=False)
    if(r < L[0]):
        r = L[0]
    
print(r)
'''


#행의 개수 N, 열의 개수 M
N, M = map(int, input().split())

r = 0

for i in range(N):
    L = list(map(int, input().split()))
    t = min(L)
    r = max(r, t)
    
print(r)