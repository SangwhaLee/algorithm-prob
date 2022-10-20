const inputs = [
  [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
  [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
  [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
]

function solution(K, N, M, chargers) {
  // solution 함수 완성
  for(let i=0;i<M;i++){
    if(chargers[i+1] - chargers[i] > K){
      console.log(0)
      return;
    }
  }

  let road = new Array(N+1).fill(0);

  for(let k=0;k<M;k++){
    road[chargers[k]] = 1
  }

  let now = 0
  let cnt = 0
  while(now < N+1){
    now += K
    if(now >= N) break
    if(road[now] === 1){
      cnt += 1
      continue
    }
    now -= 1
    while(road[now] === 0){
      now -= 1
    }
    cnt += 1
  }

  console.log(cnt)

}

for (const input of inputs) {
  solution(input[0], input[1], input[2], input[3])
}

