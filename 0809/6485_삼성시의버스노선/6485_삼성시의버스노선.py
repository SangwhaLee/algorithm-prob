import sys

sys.stdin = open('s_input.txt','r')

T = int(input())

for tc in range(T):
    bus_line = []
    N = int(input())

    for i in range(N):
        tmp = list(map(int, input().split()))
        bus_line.append(tmp)
    
    P = int(input())
    station = []
    for i in range(P):
        station.append(int(input()))

    result = [0]*P
    # print(bus_line)
    # print(station)
    for i in range(P):
        for j in range(N):
            if bus_line[j][0] <= station[i] <= bus_line[j][1]:
                result[i] += 1

    print("#{}".format(tc+1),end=' ')
    for i in range(P):
        if i == P-1:
            print(result[i])
        else:
            print(result[i], end=' ') 