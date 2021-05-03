'''
내 코드 완벽해 백점 만점
'''

#N이 1이 될때까지, K연산
N, K = map(int, input().split())
result = 0
while(True):
    if(N < K):
        result += (N - 1)
        print(result)
        break
    else:
        result += (1+N%K)
        N = N//K
