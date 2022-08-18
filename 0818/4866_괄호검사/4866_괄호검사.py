import sys
sys.stdin = open('sample_input.txt','r')

for tc in range(1,int(input())+1):
    line = input()
    stack = []
    top = -1

    for i in line:
        # 입력받는 값이 ( 이거나 { 인 경우엔 스택에 저장한다
        if i == '(' or i == '{':
            stack.append(i)
            top += 1
        # ) 입력받은 경우, 스택에 가장 최근값이 ( 이 아니거나 혹은 스택이 비어있는 경우앤
        # 잘못된 괄호쌍으로 인식한다
        elif i == ')':
            if top == -1 or stack[top] != '(':
                # 입력받는 문자열의 첫 값이 ) 인 경우 top은 그대로 -1을 유지하기 떄문에
                # 이를 방지하고자 넣은 연산이다
                top += 1
                break
            else:
                stack.pop()
                top -= 1
        # } 를 입력받은 경우도 )의 경우와 동일하다
        elif i == '}':
            if top == -1 or stack[top] != '{':
                top += 1
                break
            else:
                stack.pop()
                top -= 1

    if top == -1:
        print("#{} 1".format(tc))
    else:
        print("#{} 0".format(tc))