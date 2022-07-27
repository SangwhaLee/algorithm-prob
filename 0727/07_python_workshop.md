### 1.
1. faker라는 이름의 파이썬 라이브러리 패키지를 다운 받기 위한 명령어 이다. 터미널 창에서 실행하면 된다.
2. 

### 2.
1. faker 패키지에서 Faker 모듈을 import하기 위한 코드이다
2. Faker는 생성자 메서드, fake는 faker의 인스턴스이다.
3. name()은 fake의 메서드이다. 

### 3.

```py
class Faker():

    def __init__(self, language):
        pass

```

### 4.

1. 
```py
from faker import Faker
import random

fake1 = Faker('ko_KR')
Faker.seed(87654321)

print(fake1.name())  #이진호

fake2 = Faker('ko_KR')
print(fake2.name())  #강은주
```

seed()는 클래스 메서드로 Faker.seed() 한번의 호출을 통해 fake1과 fake2의 시드가 동일하게 적용되었다. 코드를 여러번 실행해도 결과는 같았다.

2. 
```py
from faker import Faker
import random

fake1 = Faker('ko_KR')
fake1.seed_instance(87654321)

print(fake1.name())  #이진호

fake2 = Faker('ko_KR')
print(fake2.name())  #하광수
```

seed_instance()는 인스턴스 메서드로 fake1에서만 호출하였기 때문에 fake1에만 적용된다. 코드를 여러번 실행하면 fake1은 항상 이진호지만 fake2의 값은 매번 바뀐다.