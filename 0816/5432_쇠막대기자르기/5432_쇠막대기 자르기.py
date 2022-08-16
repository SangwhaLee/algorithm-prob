import sys

sys.stdin = open('sample_input.txt','r')

for tc in range(1,1+int(input())):
    stack = []
    arr = input()
    length = 0
    for i in arr:
        length += 1

    total = 0

    for i in range(length):
        # 레이저가 위치하는 곳은 정수 1을 stack에 저장
        if arr[i] == '(' and arr[i+1] == ')':
            stack.append(1)
        # 쇠막대기의 시작점이 되는 부분은 (을 그대로 저장
        elif arr[i] == '(' and arr[i+1] != ')':
            stack.append('(')
        # 쇠막대기에 끝나는 점이 보일 때 (를 만날때까지 stack의 위에서 부터 꺼낸다
        # 꺼낸 정수 값은 lazer변수에 저장하여 해당 쇠막대기가 몇 개의 레이저에 의해 절단 되는지 확인한다
        # 총 절단된 쇠막대기 수에 현재 닫힌 쇠 막대기가 잘려진 총 갯수를 저장한 뒤 레이저의 수는 다시 stack의 맨위에 저장
        # 그래야 아직 닫히지 않는 쇠막대기들도 해당 레이저를 사용할 수 있기 떄문에
        elif arr[i] == ')' and arr[i-1] != '(':
            lazer = 0
            s_length = 0
            # len()를 죽어도 안쓰고 싶었지만 안쓰고 구현하기엔 실력이 너무 부족하여 이번 한번만 쓰게 됐습니다 ...
            while stack[len(stack)-1] != '(':
                lazer += stack.pop()
            stack.pop()
            total += (lazer+1)
            stack.append(lazer)

    print("#{} {}".format(tc, total))