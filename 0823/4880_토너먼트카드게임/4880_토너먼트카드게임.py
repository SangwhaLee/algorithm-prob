import sys

sys.stdin = open('sample_input.txt','r')

# 가위바위보의 결과를 반환하는 함수
def tournament(left, right):
    if cards[left] == 1 and cards[right] == 2:
        return right
    elif cards[left] == 2 and cards[right] == 3:
        return right
    elif cards[left] == 3 and cards[right] == 1:
        return right
    else:
        return left

# 학생들이 2명 보다 많을 경우 반으로 나눠 가위바위보를 겨루도록 하는 함수
# 한명만 있을땐 그 한명을 반환
# 2명 초과시 반으로 나눠 중간값을 구한 뒤 이 함수를 좌측면과 우측면으로 다시 실행
# 위의 동작으로 인해 학생은 항상 한 명 혹은 2명으로 나누어진다
# 2명으로 나누어진 경우 tournament 함수를 통해 두 학생이 가위바위보를 하도록 하며 그 결과를 반환
def divide_two(left, right):
    if left == right:
        return left

    mid = (left+right) // 2

    nleft = divide_two(left, mid)
    nright = divide_two(mid+1, right)
    return tournament(nleft, nright)

for tc in range(1,int(input())+1):
    N = int(input())
    cards = list(map(int,input().split()))

    print("#{} {}".format(tc, divide_two(0, N-1)+1))

