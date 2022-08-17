import sys
sys.stdin = open('input.txt','r')

for tc in range(1,int(input())+1):
    stack = []
    top = -1
    arr = input()
    #print(arr)
    for i in arr:
        # 입력받은 값이 (이면 스택에 넣어준다
        if i == '(':
            stack.append(i)
            top += 1
        # 입력 받은 값이 )일 경우 앞서 저장되어있는 )가 있을 경우 뒤에 뭐가 나와도 올바른
        # 괄호 쌍이 될 수는 없기 때문에 바로 반복문을 탈출해준다
        # 만약 앞선 ( 값이 있는 경우 입력받은 )과 짝이되어 스택에서 빼준다
        else:
            if '(' not in stack:
                stack.append(i)
                top += 1
                break
            else:
                stack.pop()
                top -= 1

    #print(stack)
    # 최종적으로 top의 값이 -1인 경우 괄호의 쌍이 깔끔하게 맞아 떨어진 경우이고
    # 만약 -1이 아닌경우 스택에 짝이 되지 못한 괄호가 남아 있다는 것이다
    if top == -1:
        print("#{} 1".format(tc))
    else:
        print("#{} -1".format(tc))