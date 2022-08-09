import sys

sys.stdin = open('sample_input.txt','r')

N = int(input())

for i in range(N):
    numb = int(input())
    numbers = list(map(int,input().split()))
    maxV = numbers[0]
    minV = numbers[0]

    for j in numbers:
        if j > maxV:
            maxV = j
        if j < minV:
            minV = j
    print("#{} {}".format(i+1, maxV-minV))