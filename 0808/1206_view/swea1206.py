#1206_view
# 220808

# 정답코드

import sys

sys.stdin = open('input.txt','r')

T = int(input())
cnt = 0

tower = list(map(int, input().split()))

for k in range(1,11):
    for i in range(2,T-2):
        maxT = 0
        for j in range(i-2, i+3):
            if j != i and tower[j] > maxT:
                maxT = tower[j]
        if tower[i] - maxT > 0:
            cnt += tower[i] - maxT

    print('#{} {}'.format(k, cnt))

