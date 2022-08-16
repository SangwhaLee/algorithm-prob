import sys
sys.stdin = open('sample_input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    # 학생들 출발, 도착 방정보를 저장할 리스트
    students = []
    # 학생들의 경로를 체크할 리스트
    check = [0]*201

    # 학생들의 출발, 도착 방 정보를 입력받고 저장
    for i in range(N):
        tmp = list(map(int, input().split()))
        students.append(tmp)

    # 저장한 방 정보에 따라 맞는 경로에 하나씩 추가
    for i in students:
        if i[0]%2:
            a = i[0]//2 + 1
        else:
            a = i[0]//2
        if i[1]%2:
            b = i[1]//2 + 1
        else:
            b = i[1]//2

        if a < b:
            for j in range(a, b+1):
                check[j] += 1
        else:
            for j in range(b, a+1):
                check[j] += 1

    maxV = check[0]
    # 체크 리스트에서 최대값이 바로 모든 학생이 지나간 최소한의 시간과 동일
    for i in check:
        if i > maxV:
            maxV = i

    print("#{} {}".format(tc, maxV))