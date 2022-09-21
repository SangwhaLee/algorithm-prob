def selection_sort(A):
    if A != []:
        minimum = min(A)
        A.remove(minimum)
        return [minimum] + selection_sort(A)
    else:
        return []


a = [4, 3, 2, 5, 6, 1]

print(selection_sort(a))