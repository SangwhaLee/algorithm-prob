import sys

sys.stdin = open('sample_in.txt','r',encoding='UTF8')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    station = [0] * 1001
    for k in range(N):
        bus_type, start_num, end_num = map(int, input().split())
        station[start_num] += 1
        station[end_num] += 1

        if bus_type == 1: #일반 버스는 전부 정차
            for i in range(start_num+1, end_num):
                station[i] += 1
        elif bus_type == 2:#버스가 급행인 경우
            if start_num%2: #시작 번호가 홀수면
                for i in range(start_num+1, end_num):
                    if i%2:
                        station[i] +=1
            else:
                for i in range(start_num+1, end_num):
                    if i%2 == 0:
                        station[i] +=1
        else: #버스가 광역 급행인 경우
            if start_num%2: #시작 번호가 홀수면
                for i in range(start_num+1, end_num):
                    if i%3 == 0 and i%10:
                        station[i] +=1
            else:#시작번호가 짝수인 경우
                for i in range(start_num+1, end_num):
                    if i%4 == 0:
                        station[i] +=1

    maxV = station[0]
    for i in station:
        if i > maxV:
            maxV = i

    print("#{} {}".format(tc,maxV))