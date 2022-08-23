import sys
sys.stdin = open('input.txt','r')

for tc in range(1,11):
    N = int(input())

    arr = list(input())
    # 후위 표기법으로 변환 후 저장할 리스트
    profix = []
    stack = []
    top = -1
    # 스택 내부의 연산자의 우선순위
    isp = { '*':2, '/':2, '+':1, '-':1, '(':0, }
    # 식 내부의 연산자의 우선순위
    icp = { '*':2, '/':2, '+':1, '-':1, '(':3, }

    # 만약 식의 토큰이 피연산자(숫자)일 경우 바로 후위표기식 리스트에 저장하고
    # 토큰이 연산자인 경우 스택의 top값과 우선순위를 비교하여 토큰이 더 크면 스택에 저장하고
    # 반대의 경우 스택의 top을 하나 제거하고 그 다음에 스택에 토큰을 저장한다
    for i in range(N):
        if arr[i].isdigit():
            profix.append(arr[i])
        else:
            if top == -1:
                stack.append(arr[i])
                top += 1
            # 식의 토큰이 )일 경우 스택에서 (가 나올때까지 top값을 제거
            elif arr[i] == ')':
                while stack[top] != '(':
                    profix.append(stack.pop())
                    top -= 1
                stack.pop()
                top -= 1
            else:
                # 토큰과 스택의 top값의 우선순위를 비교
                if isp[stack[top]] < icp[arr[i]]:
                    stack.append(arr[i])
                    top += 1
                else:
                    profix.append(stack.pop())
                    stack.append(arr[i])

    #print(profix)
    calcul = []
    top = -1

    # 후위표기식에서 피연산자 (숫자)는 바로 스택에 저장하고 연산자가 나올 경우 연산에 필요한
    # 피연산자의 개수만큼 스택에서 pop 그 후 연산을 한 값을 다시 스택에 저장
    # 이것을 식의 길이만큼 반복 한 뒤 마지막으로 스택에 남은 하나의 숫자가 답이 된다.
    for i in profix:
        if i.isdigit():
            calcul.append(int(i))
        else:
            c1 = calcul.pop()
            c2 = calcul.pop()
            top -= 2
            if i == '+':
                calcul.append(c1+c2)
                top += 1
            elif i == '*':
                calcul.append(c1*c2)
                top += 1
            elif i == '/':
                calcul.append(c2/c1)
                top += 1
            else:
                calcul.append(c2-c1)
                top += 1

    ans = calcul.pop()

    print("#{} {}".format(tc, ans))