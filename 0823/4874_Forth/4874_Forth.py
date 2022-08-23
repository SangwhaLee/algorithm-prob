import sys

sys.stdin = open('sample_input.txt','r')

for tc in range(1,int(input())+1):
    stack = []
    top = -1
    arr = list(input().split())

    # 식의 토큰이 숫자일 경우 스택에 저장한다
    for i in arr:
        if i.isdigit():
            stack.append(int(i))
            top += 1
        # 식의 토큰이 문자일 경우
        else:
            # 토큰의 값이 .이라면 스택에 마지막으로 남아있는 숫자를 pop한다
            # 숫자가 마지막으로 남아있어야 하므로 숫자가 2개 이상있거나 남아있는 값이
            # 숫자가 아닐 경우 error 출력
            if i == '.':
                if top > 0:
                    ans = 'error'
                    break
                else:
                    ans = stack.pop()
                    top -= 1
            # 토큰이 연산자 문자일 경우 스택에서 피연산자 두개를 pop해야 하므로 이 때
            # 스택에 저장된 값의 개수가 2개 이하라면 error 출력
            else:
                if top < 1:
                    ans = 'error'
                    break
                c1 = stack.pop()
                c2 = stack.pop()
                if (not str(c1).isdigit()) or (not str(c2).isdigit()):
                    ans = 'error'
                    break
                top -= 2
                if i == '+':
                    stack.append(c1+c2)
                    top += 1
                elif i == '*':
                    stack.append(c1*c2)
                    top += 1
                # 나눗셈은 항상 나누어 떨어지기 때문에 소수점은 필요가 없다
                elif i == '/':
                    stack.append(c2//c1)
                    top += 1
                else:
                    stack.append(c2-c1)
                    top += 1

    print("#{} {}".format(tc, ans))