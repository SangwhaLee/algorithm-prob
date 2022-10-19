// 1번
const nums = [1,2,3,4,5,6,7,8]

for (const i = 0; i < nums.length; i++) {
  console.log()
}

// for (const i = 0; i < nums.length; i++) {
//                                     ^

// TypeError: Assignment to constant variable.
/* 1번 오류가 발생하는 이유는 i는 현재 상수인 const로 정의되어있다
 하지만 for문 조건식을 달성할 때까지 i의 값에 변화가 일어나는데 상수로
 지정된 값은 재할당이나 값의 변경이 불가능하기 때문에 오류가 일어난다.*/


// 2번
for (num in nums) {
  console.log(num, typeof num)
}

// 0 string
// 1 string
// 2 string
// 3 string
// 4 string
// 5 string
// 6 string
// 7 string
/* for ~ in 구문을 사용할 경우 해당 객체의 키값에 접근하게 되어
위와 같은 결과가 나온 것이다. array 내부의 값을 출력하고 싶다면
in이 아니라 of를 사용해야 한다.
*/