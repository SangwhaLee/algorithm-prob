import sys


for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, sys.stdin.readline().split())

    result = 'a'
    if (q2 < y1) or (x2 > p1) or (y2 > q1) or (p2 < x1):
        result = 'd'

    if x2 == p1:
        if (q1 == y2) or (q2 == y1):
            result = 'c'
        else:
            result = 'b'
    if q2 == y1:
        if (x2 == p1) or (x1 == p2):
            result = 'c'
        else:
            result = 'b'
    if x1 == p2:
        if (y1 == q2) or (q1 == y2):
            result = 'c'
        else:
            result = 'b'
    if y2 == q1:
        if (x2 == p1) or (x1 == p2):
            result = 'c'
        else:
            result = 'b'

    print(result)


