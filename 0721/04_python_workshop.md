### 1.
```py
N = int(input())

for i in range(1,N+1):
    if N%i == 0:
        print(i, end=' ')
```

### 2. 
```py
def list_sum(num_list):
    total = 0
    for i in num_list:
        total += i
    return total
```

### 3.
```py
def dict_list_sum(dict_list):
    total = 0
    for dic in dict_list:
        total += dic['age']
    return total
```

### 4.
```py
def all_list_sum(all_list):
    total = 0
    for i in all_list:
        for j in i:
            total += j
    return total

```


### 5. 
```py
def get_secret_word(num_list):
    result = ""
    for i in num_list:
        result += chr(i)
    return result
```

### 6.
```py
def get_secret_number(word):
    total = 0
    for i in word:
        total += ord(i)
    return total
```

### 7.
```py
def get_strong_word(word1, word2):
    total1 = 0
    total2 = 0
    for i in word1:
        total1 += ord(i)
    for i in word2:
        total2 += ord(i)
    if total1 > total2:
        return word1
    elif total2 > total1:
        return word2
    else:
        return [word1, word2]
```