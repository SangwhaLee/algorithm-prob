import sys

sys.stdin = open('input1.txt','r',encoding='UTF8')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = input()

    i = 0
    cnt = 1
    maxV = 1
    while i < N:
        if arr[i] == '1':
            m = i
            while m+1 < N and arr[m+1] == '1':
                m += 1
                cnt += 1
                i = m
            if cnt > maxV:
                maxV = cnt
                cnt = 1
        i += 1
    print("#{} {}".format(tc, maxV))