import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(T):
    N, Q = map(int, input().split())
    boxes = [0]*N
    for i in range(1,Q+1):
        L, R = map(int,input().split())
        for j in range(L-1,R):
            boxes[j] = i
    
    print("# {}".format(tc+1), end=' ')
    for i in range(N):
        if i == N-1:
            print(boxes[i])
        else:
            print(boxes[i],end=' ')
