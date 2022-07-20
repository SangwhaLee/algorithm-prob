### 1.

```py
number = int(input('숫자를 입력하시오: '))

for i in range(1,number+1):
    print(i)

```

### 2.

```py
number = int(input('숫자를 입력하시오: '))

for i in range(1,number+1):
    print(i, end=' ')

```

### 3.

```py
number = int(input('숫자를 입력하시오: '))

for i in range(number,-1,-1):
    print(i)
```

### 4.
```py
number = int(input('숫자를 입력하시오: '))

for i in range(number,-1,-1):
    print(i, end=' ')
```

### 5.
```py
number = int(input('숫자를 입력하시오: '))
num_sum = 0
for i in range(1,number+1):
    num_sum += i

print(num_sum)
```

### 6.
```py
number = int(input('숫자를 입력하시오: '))

for i in range(number):
    for j in range(number):
        print('*',end='')
    print()
```

### 7.

```py
numbers = list(map(int, input().split()))

def get_len_list(S):
    cnt = 0
    for i in S:
        cnt += 1
    return cnt

length = get_len_list(numbers)

def bubble_sort(S, length):
    for i in range(0,length-1):
        for j in range(1,length-i):
            if S[j-1] > S[j]:
                S[j-1] , S[j] = S[j], S[j-1]

if length%2:
    print(numbers[length//2])
else:
    print(numbers[length//2-1], numbers[length//2])

```