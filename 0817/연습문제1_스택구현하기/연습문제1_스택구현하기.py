stack = [0]*3
top = -1

# 스택의 push 메서드와 같은 효과를 내도록 설계한다
def push(item, size):
    # top값은 글로벌로 사용한다
    global top
    top += 1
    # 만약 stack이 꽉차 있는데 push하는 경우
    if top == size:
        print('overflow!')
    else:
        stack[top] = item

def pop():
    global top
    # 만약 스택이 비어있는데 pop하는 경우
    if top == -1:
        print('underflow')
        return
    else:
        tmp = stack[top]
        top -= 1
        return tmp


nums = list(map(int, input().split()))

for i in nums:
    push(i, 3)

print(stack)

for i in range(4):
    print(pop())