import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    two = 0
    three = 0
    five = 0
    seven = 0
    eleven = 0

    while N%2 == 0:
        N /= 2
        two += 1
    while N%3 == 0:
        N /= 3
        three += 1
    while N%5 == 0:
        N /= 5
        five += 1
    while N%7 == 0:
        N /= 7
        seven += 1
    while N%11 == 0:
        N /= 11
        eleven += 1
    
    print("#{} {} {} {} {} {}".format(tc+1, two, three, five, seven, eleven))