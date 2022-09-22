# import sys
# sys.stdin = open('input.txt','r')


def change_page(N, idx):
    global maximum
    if N == num:
        maximum = max(int(''.join(origin)), maximum)
        return

    for i in range(idx, len(origin)):
        for j in range(i+1, len(origin)):
            if origin[i] <= origin[j]:
                origin[i], origin[j] = origin[j], origin[i]
                change_page(N+1, i)
                origin[i], origin[j] = origin[j], origin[i]

    if not maximum and N < num:
        rotate = (num-N) % 2
        if rotate:
            origin[-1], origin[-2] = origin[-2], origin[-1]
        change_page(N+1, idx)


for tc in range(1, int(input())+1):
    origin, num = input().split()
    num = int(num)
    origin = list(origin)
    maximum = 0
    # print(num, origin)
    change_page(0, 0)
    print("#{} {}".format(tc,maximum))