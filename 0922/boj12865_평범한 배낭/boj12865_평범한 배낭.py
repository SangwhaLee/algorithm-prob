N, K = map(int,input().split())

dp = list([0]*(K+1) for _ in range(N+1))

for i in range(0,K+1):
    dp[0][i] = 0
for i in range(0, N+1):
    dp[i][0] = 0

weight = []
value = []
for i in range(N):
    tmp = list(map(int,input().split()))
    weight.append(tmp[0])
    value.append(tmp[1])

for i in range(1,N+1):
    for j in range(1,K+1):
        if weight[i-1] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i-1]]+value[i-1])

        else:
            dp[i][j] = dp[i-1][j]

maximum = 0
for i in range(N+1):
    for j in range(K+1):
        if dp[i][j] > maximum:
            maximum = dp[i][j]

print(maximum)


