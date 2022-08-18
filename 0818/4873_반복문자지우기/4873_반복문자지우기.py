import sys
sys.stdin = open('sample_input.txt','r')

for tc in range(1,int(input())+1):
    # 문자열을 입력
    letters = input()
    # 스택을 저장할 리스트 생성
    stack = []
    top = -1
    for i in letters:
        # 만약 스택이 비어있지 않거나 스택 맨위의 값이 i와 동일하다면 두값을 제거
        if top != -1 and stack[top] == i:
            top -= 1
            stack.pop()
        # 스택이 비어있거나 앞선 값이 i와 동일하지 않다면 스택에 추가
        else:
            stack.append(i)
            top += 1

    print("#{} {}".format(tc, top+1))

    # 스택의 크기를 미리 짜놓고 top만 조작하여 답을 구하는 방법도 있지만 len() 사용하지 않고싶어서 이렇게 풀었다