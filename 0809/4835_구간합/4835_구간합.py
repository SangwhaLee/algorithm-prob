import sys

sys.stdin = open('sample_input.txt','r')

T = int(input())

for i in range(T):
    N, M = map(int,input().split())

    numbers = list(map(int,input().split()))

    maxV=0
    minV=1000000 #조건상 가장 높게 나오는 수보다 큰 수

    for j in range(N-M+1):#전체 범위에서 M만큼 뺀 수까지
        total = 0
        for k in range(j,j+M):#연속이기 때문에 M만큼 반복
            total += numbers[k]
        # print(total)
        if total > maxV:
            maxV = total
        if total < minV:
            minV = total

    print("#{} {}".format(i+1,maxV-minV))