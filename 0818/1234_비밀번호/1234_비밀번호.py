import sys
sys.stdin = open('input.txt','r')

for tc in range(1, 11):
    # 먼저 둘다 str형 그대로 입력 받는다
    n, word = input().split()
    # n은 int()를 사용하여 정수로 변환한다
    N = int(n)
    # 문자를 하나하나 처리해나갈 스택 선언
    # 문자열의 길이도 알고 있기 때문에 스택의 길이를 미리 선언하고 top만을 활용할 까 했지만
    # 그럴경우 스택 내부에 없어야 할 값이 존재하기 때문에 결국 빈 리스트로 선언
    stack = []
    top = -1

    for i in word:
        # 만약 스택 내부에 값이 없거나 스택 맨위의 값이 현재 값과 동일하지 않다면 스택에 저장
        if top == -1 or stack[top] != i:
            stack.append(i)
            top += 1
        # 만약 스택 맨위의 값이 현재와 동일하다면 그 값을 스택에서 제거
        else:
            stack.pop()
            top -= 1

    # 스택에 남아있는 값들을 모두 모은다
    ans = ''.join(stack)
    print("#{} {}".format(tc, ans))
