### 1.
 
Python에 기본적으로 정의되어 있는 클래스로는 
int, float, range, tuple, list



### 2. 

__init__은 클래스의 생성자로 객체의 초기화를 위한 함수 있다.
클래스를 인스턴스화 할때 반드시 처음에 호추로디는 특수한 함수

__del__은 소멸자로 객체를 지울때 클래스나 인스턴스에 어떤 변화를 주기 위해 사용된다.

__str__은 객체의 정보를 반환하는데 있어서 어떤 형식으로 반환할 것인지를 정하는 메서드, 다른 자료형 간에 인터페이스를 제공하기 위한 존재 

__repr__은 __str__과 유사하게 정보를 반환하는데 있어서 어떤 형식으로 반환할 것인지를 정하는 메서드이지만 사용자 즉 인간이 이해할 수 있는 표현으로 나타내기 위한 용도

### 3.

1. .append() 리스트에 전달된 인자를 추가하는 메서드

2. .count() 리스트, 문자열, 등 전달된 인자와 동일한 값이 몇개 포함되었는지 반환하는 메서드

3. .reverse() 시퀸스형 iterable의 순서를 반대로 뒤집어 놓는 메서드

### 4.

1. ZeroDivisionError : 나눗셈 연산 시 0으로 나눴을때 
2. NameError : namespace에 이름이 존재하지 않을 때
3. TypeError : 메서드에 처리 되지 못하는 type을 입력했을 때
4. IndexError : index가 범위를 벗어났을 때
5. KeyError : 딕셔너리에서 잘못된 key를 호출했을 때
6. ModuleNotFoundError : 잘못된 모듈을 import 했을 때
7. ImportError : 메인 파일에 상대 경로르 사용했을 때
