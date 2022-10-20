function findQueens(n) {
	// 이곳에 작성합니다.
  let answer = 0

  const dfs = (board, row) => {
    if(row === n) return answer++
    for(let i=1 ;i<=n ;i++){
      board[row+1] = i
      if(check(row+1, board)) dfs(board, row+1)
    }
  }

  const check = (row, board) => {
    for(let i=0;i<row;i++){
      if(board[i] === board[row]) return false
      if(Math.abs(i-row) === Math.abs(board[row] - board[i])) return false
    }
    return true
  }

  for(let i=1;i<=n;i++){
    let board = new Array(n+1).fill(0)
    board[1] = i;
    dfs(board, 1)
  }

  return answer
}

console.log(findQueens(4)) // 2