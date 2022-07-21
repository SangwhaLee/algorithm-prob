### 1.

```py
ssafy(name=' 승호','광주')
```

### 2.
```py
def my_avg(x, *num_list):
    return sum(num_list)/len(num_list)

print(my_avg(77, 83, 95, 80, 70))
```

### 3.

10이 저장된다. my_func()함수로 3,7이 인자로 전달되었고 함수 내부의 계산결과로 인해 10이 저장된다.

### 4.

LEGB
local space -> enclosed space -> global space -> built-in space

### 5. 

(2) 함수에서 return을 작성하지 않을면 None 값을 반환한다.

### 6.

**장점**
1. 재귀는 반복문에 비해 이해하기 쉽다. 재귀함수가 어울리는 논리 흐름이 존재한다.
2. 코드가 간결해진다.
3. 사용되는 변수가 줄어든다.

**단점**
1. 재귀의 깊이가 깊어지면 StkacOverFlow가 발생할 가능성이 높다.
2. base case를 제대로 정해놓지 않을 시 무한반복이 일어나고 CPU크래쉬가 발생



