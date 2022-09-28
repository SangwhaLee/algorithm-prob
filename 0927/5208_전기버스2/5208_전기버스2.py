import sys
sys.stdin = open('sample_input.txt','r')


def charge_station(depth, ccnt):
    global minimum
    if depth >= N:
        minimum = min(ccnt, minimum)
        return

    if ccnt >= minimum:
        return

    count = station[depth]
    for i in range(count,0, -1):
        charge_station(depth+i, ccnt+1)


for tc in range(1, int(input())+1):
    station = list(map(int,input().split()))
    N = station[0]
    station[0] = 0

    minimum = 1e9

    charge_station(1, -1)
    print("#{} {}".format(tc, minimum))