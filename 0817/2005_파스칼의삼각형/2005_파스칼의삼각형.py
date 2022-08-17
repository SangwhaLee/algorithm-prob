import sys
sys.stdin = open('input.txt','r')

for tc in range(1,int(input())+1):
    N = int(input())

    # 삼각형 모양의 이차원 리스트를 만들어 준다
    pascal = [[0]*i for i in range(1,N+1)]

    # 파스칼의 삼각형의 각 줄의 시작과 끝은 항상 정수 1을 가지도록 저장한다
    for i in range(N):
        pascal[i][0] = 1
        pascal[i][i] = 1

    # 삼각형내의 모든 값을 순회하며 만약 그 위치가 비어있을 경우 (값이 0이면 된다)
    # 해당 위치의 값은 자신의 위치 기준으로 위줄의 양쪽 두 값을 더한 값과 같다
    for i in range(N):
        for j in range(i):
            if pascal[i][j] == 0:
                pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]

    print("#{}".format(tc))
    for i in range(N):
        for j in range(i+1):
            print(pascal[i][j],end=' ')
        print()
