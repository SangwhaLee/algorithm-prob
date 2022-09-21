import sys
sys.stdin = open('input.txt','r')


def change_page(N, idx):
    global maximum
    if N == 0:
        total = 0
        std = 10**(len(origin)-1)
        for i in origin:
            total += i*std
            std //= 10

        if total > maximum:
            maximum = total


    for i in range(idx, len(origin)-1):
        for j in range(idx+1, len(origin)):
            origin[i], origin[j] = origin[j], origin[i]
            change_page(N-1, idx+1)
            origin[i], origin[j] = origin[j], origin[i]


for tc in range(1, int(input())+1):
    origin, num = map(int, input().split())
    num = int(num)
    origin = list(map(int,str(origin)))
    maximum = 0
    print(num, origin)
    change_page(num, 0)
    print(maximum)