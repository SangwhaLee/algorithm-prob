### 1.
```py
def count_vowels(word):
    cnt = 0
    cnt += word.count('a')
    cnt += word.count('e')
    cnt += word.count('i')
    cnt += word.count('o')
    cnt += word.count('u')
    return cnt
```

### 2.

(4)번 .strip([.chars])에서 []는 값을 입력하지 않아도 된다는 뜻이다. 

### 3. 

```py
def only_square_area(list1, list2):
    area = 0
    for i in list1:
        if i in list2:
            area += i**2
    
    return area
```