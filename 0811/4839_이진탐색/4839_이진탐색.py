import sys

sys.stdin = open('sample_input.txt','r')

def binary_search(P, target): #이분탐색이 이뤄지는 함수
    left = 1
    right = P
    cnt = 0
    while left <= right:
        mid = (left + right) // 2
        cnt += 1
        if mid < target:
            left = mid
        elif mid > target:
            right = mid
        else:
            return cnt

T = int(input())

for tc in range(T):
    P, A, B = map(int, input().split())
    aCnt = binary_search(P, A) # A 타겟을 찾기 위한 이분탐색
    bCnt = binary_search(P, B) # B타겟을 찾기 위한 이분탐색

    if aCnt < bCnt:
        print("#{} A".format(tc+1))
    elif bCnt < aCnt:
        print("#{} B".format(tc + 1))
    else:
        print("#{} 0".format(tc + 1))