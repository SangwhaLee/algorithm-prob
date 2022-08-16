import sys

sys.stdin = open('input.txt','r')

for tc in range(1,int(input())+1):
    # 원재가 거래할 총 날짜
    days = int(input())
    # 날짜별 매매가
    sales = list(map(int,input().split()))
    # 총 이익
    total = 0

    # 날짜별 매매가에서 가장 뒤의 값을 max값으로 설정
    maxV = sales[days-1]

    # 뒤에서 부터 매매가를 확인하여 현재의 최대값보다 작으면 최대값에서 뺸값 만큼 총이익에 더하고
    # 최대값보다 클 경우 최대값 교체
    for i in range(days-1,-1,-1):
        if sales[i] < maxV:
            total += maxV - sales[i]
        elif sales[i] > maxV:
            maxV = sales[i]

    print("#{} {}".format(tc, total))