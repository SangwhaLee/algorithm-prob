from collections import deque

N, k = map(int, input().split())

belt = list(map(int,input().split()))


while True:
    # 1. 회전: belt의 각 구성요소를 다음 인덱스로 이동 마지막 인덱스에 있는 값은 첫 인덱스로 이동
    # 2. 가장 뒤쪽에 있는 로봇의 다음 인덱스가 비어있다면 이동, 로봇이 이