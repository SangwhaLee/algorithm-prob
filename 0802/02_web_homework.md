### 1.
- header
- section
- footer


### 2.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <form action="">
    <div>
      <label for="username">USERNAME:</label>
      <input type="text" name="username" placeholder="아이디를 입력 해 주세요." id="username" autofocus>
    </div>
    <div>
      <label for="password">PWD:</label>
      <input type="password" name="password" id="password">
      <input type="submit" value="로그인">
    </div>
  </form>
</body>
</html>
```

### 3.

rem

### 4.

자손 결합자의 경우 div 안에 있는 모든 p의 텍스트 색이 crimson으로 바뀐다.
자식 결합자의 경우 div 직계에 자식에 속한 p의 색만 바뀐다 예를 들어 다른 <span>안에 p가 있을 경우 해당 p의 색은 바뀌지 않는다.