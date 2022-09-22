import sys
sys.stdin = open('sample_input.txt','r')

for tc in range(1, int(input())+1):
    N = int(input())
    schedule = []
    for i in range(N):
        tmp = list(map(int,input().split()))
        schedule.append(tmp)

    schedule.sort(key=lambda x: (x[1],x[0]))

    cnt = 1
    now = schedule[0]

    for sc in schedule:
        if sc[0] >= now[1]:
            cnt += 1
            now = sc

    print("#{} {}".format(tc, cnt))