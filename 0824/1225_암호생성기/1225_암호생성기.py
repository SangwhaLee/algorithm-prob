import sys

sys.stdin = open('input.txt','r')

for tc in range(1, 11):
    N = int(input())
    # 8자리 숫자를 입력받는다
    arr = list(map(int,input().split()))
    # 암호문을 만들기 위한 큐를 생성
    Q = []
    
    # 맨끝자리를 제외한 7자리 숫자를 넣는다
    for i in range(7):
        Q.append(arr[i])

    # new 변수에 맨끝자리 값을 저장
    new = arr[7]
    # 단계별로 빼야할 수가 달라지므로 이를 위한 변수
    m = 1

    # 맨끝에 붙어야할 숫자가 0보다 같거나 작아지면 반복문 종료
    while new > 0:
        # 맨끝자리에 new 변수 추가
        Q.append(new)
        # new 변수는 Q에서 dequeue한 뒤 그 값에서 m을 뺸값이 된다.
        new = Q.pop(0) - m
        # 만약 m의 값이 5라면 사이클이 돌았으므로 m을 1로 초기화
        if m == 5:
            m = 1
        else:
            m += 1
    
    # 마지막 new의 값이 음수일 수 도 있으므로 0으로 고정
    new = 0
    Q.append(new)
    
    print("#{}".format(tc), end = ' ')
    for i in Q:
        print(i, end=' ')
    print()
