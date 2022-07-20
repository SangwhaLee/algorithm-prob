### 1.
```py
sum()
len()
abs()
list()
range()
```

### 2.
```py
num = list(range(1,51)[0:51:2])

```

### 3.
```py
n = 5
m = 9

for i in range(m):
    for j in range(n):
        print('*', end='')
    print('\n',end='')
```

### 4.
```py
temp = 36.5

S = '입실 불가' if temp >= 37.5 else '입실 가능'  
print(S)
```

### 5.
```py
def get_len_str(S):
    cnt = 0
    for i in S:
        cnt += 1
    return cnt

def get_middle_char(S):
    length = get_len_str(S)
    if length%2:
        num = length//2
        return S[num:num+1]
    else:
        num = length//2
        return S[num-1:num+1]
    
S = input()    
print(get_middle_char(S))
    
```