'''

'''

#배열의 크기 N, 숫자가 더해지는 횟수 M, 더할 수 있는 원소의 개수 K
N,M,K = map(int, input().split())
L = list(map(int, input().split()))
#L을 정렬한다.
L.sort()

'''
내 코드 : 하나는 생각하지만 둘은 생각하지 못했다! 반복되는 수의 덩어리는 구했으면 for문을 돌 필요가 없었다;
result = 0

for i in range(M):
    if((i+1) % (K+1) == 0) :
        result += L[N-2]
    else:
        result += L[N-1]

print(result)
'''

a = L[N-1] #가장 큰 수
b = L[N-2] #두번째로 큰 수

t = K*a + b #반복되는 수의 덩어리. 따라서 덩어리의 길이는 K+1이 된다.
result = t * (M//(K+1)) + a*(M%(K+1))
print(result)
