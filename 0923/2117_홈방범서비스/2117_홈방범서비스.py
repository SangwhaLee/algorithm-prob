import sys
sys.stdin = open('sample_input.txt','r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    city = list(list(map(int, input().split())) for _ in range(N))
    house_idx = []
    maxHs = 0

    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                house_idx.append((i,j))

    for k in range(1, N+2):
        for i in range(N):
            for j in range(N):
                cnt = 0
                for hs in house_idx:
                    if k > (abs(i-hs[0])+abs(j-hs[1])):
                        cnt += 1
                if (k * k + (k - 1) * (k - 1)) <= M*cnt:
                    maxHs = max(maxHs, cnt)

    print("#{} {}".format(tc, maxHs))