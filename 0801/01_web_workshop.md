### 1&2&3.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>01_web_workshop</title>
    
</head>
<body>
  <a href="https://ssafy.com"><img src="C:\Users\LG\Desktop\ssafy\HWS_PRACTICE\0801\01_web_workshop\ssafy\images\my_ssafy.png" alt="ssafy"></a>
  <img src="../images/my_ssafy.png" alt="ssafy">
    <div class="large-box">
      <div class="medium-box">
        <div class="small-box">
        </div>
      </div>
    </div> 
  
  <div id="ssafy">
    <h2>어떻게 선택 될까?</h2>
    <p>첫번째 단락</p>
    <p>두번째 단락</p>
    <p>세번째 단락</p>
    <p>네번째 단락</p>
  </div>

  <style>
    #ssafy > p:nth-of-type(2) {
      color: blue;
    }
  </style>
</body>
</html>

```

### 4. 

p:nth-child는 해당 구문의 모든 자식 속성을 그 타입과 무관하게 카운팅한다. 이 구문의 경우 자식 속성이 <p>이던 <h2>이던 상관없이 카운트 한다. 하지만 p:nth-of-type은 <p> 타입에 해당하는 자식 속성만 카운트 한다.