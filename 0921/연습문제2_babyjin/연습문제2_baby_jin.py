def selection_sort(A):
    if A != []:
        minimum = min(A)
        A.remove(minimum)
        return [minimum] + selection_sort(A)
    else:
        return []


cards = list(map(int,input().split()))
deck = [0]*10
cards = selection_sort(cards)
answer = 0

for i in cards:
    deck[i] += 1

for i in range(10):
    while deck[i] != 0:
        if deck[i] >= 3:
            deck[i] -= 3
            answer += 1
        elif deck[i+1] >0 and deck[i+2] > 0:
            deck[i] -= 1
            deck[i+1] -= 1
            deck[i+2] -= 1
            answer += 1
        else:
            break

if answer == 2:
    print("baby-jin")


