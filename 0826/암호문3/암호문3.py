import sys
sys.stdin = open('input.txt','r')

for tc in range(1, 11):
    N = int(input())
    code = list(map(int,input().split()))
    ord = int(input())
    orders = list(input().split())

    for i in range(len(orders)):
        if not orders[i].isdigit():
            if orders[i] == 'I':
                additional = []
                for j in range(int(orders[i+2])):
                    additional.append(int(orders[i+3+j]))
                tmp1 = code[:int(orders[i+1])]
                tmp2 = code[int(orders[i+1]):]
                code = tmp1 + additional + tmp2
            elif orders[i] == 'A':
                for j in range(int(orders[i+1])):
                    code.append(int(orders[i+2+j]))
            else:
                tmp1 = code[:int(orders[i+1])]
                tmp2 = code[int(orders[i+1])+int(orders[i+2]):]
                code = tmp1 + tmp2

    print("#{}".format(tc),end=' ')
    for i in range(10):
        print(code[i], end=' ')
    print()
