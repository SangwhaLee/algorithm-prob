import sys

sys.stdin = open('sample_input.txt','r')

for tc in range(1,int(input())+1):
    # 차례대로 전체 단어와 축약단어이다
    A, B = input().split()
    # 전체 단어 길이
    A_length = 0
    # 축약단어 길이
    B_length = 0

    # 전체 단어 길이를 측정
    for i in A:
        A_length += 1

    # 축약단어 길이를 측정
    for i in B:
        B_length += 1

    # 반복문 진행을 위한 현재 위치 변수
    now = 0
    # 전체 버튼 입력 횟수
    cnt = 0

    while now < A_length:
        # 만약 단어에서 지금 위치의 글자가 축약단어의 첫 글자와 같을 경우
        if A[now] == B[0]:
            # 지금 위치에서 부터 축약단어의 길이만큼 이어진 글자가 축약단어 전체와 같은 경우
            if A[now:now+B_length] == B:
                # 버튼 횟수는 한 번만 증가, 현재 위치는 축약단어의 다음 위치까지 이동
                cnt += 1
                now += B_length
                continue

        # 축약 단어를 사용하지 않을 경우 한개씩 증가
        now += 1
        cnt += 1

    print("#{} {}".format(tc, cnt))