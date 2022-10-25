// 코드를 작성해 주세요
const scissorButton = document.getElementById("scissors-button")
const rockButton = document.getElementById("rock-button")
const paperButton = document.getElementById("paper-button")
const player2Image = document.getElementById("player2-img")
const modalContent = document.querySelector(".modal-content")
const player1Image = document.getElementById("player1-img")
const modal = document.querySelector(".modal")
let p1count = 0
let p2count = 0
const countA = document.querySelector(".countA")
const countB = document.querySelector(".countB")

images = [
  "paper.png", "rock.png", "scissors.png"
]
let idx = 0

const changeIamge = function(){
  player2Image.setAttribute("src", `./img/${images[idx%3]}`)
  idx += 1
}

const totalRoatate = function(p1Value){
  player1Image.setAttribute("src", `./img/${images[p1Value]}`)
  const rotate = setInterval(changeIamge, 100)
  setTimeout(function(){
    clearTimeout(rotate)
    const p2Value = callRandomImage()
    rockScissorPaper(p1Value, p2Value)
    modal.style.display = "flex"
  }, 3000)
  modal.addEventListener("click", function(event){
    modal.style.display = "none"
  })
}

function callRandomImage(){
  const randomNumber = Math.floor(Math.random() * 3)
  player2Image.setAttribute("src", `./img/${images[randomNumber]}`)
  return randomNumber
}

function rockScissorPaper(p1, p2){
  if(p1 === p2){
    modalContent.innerText = "무승부입니다!"
  }
  else if(p1===0 && p2===2 || p1===1 && p2===0 || p1===2 && p2===1){
    modalContent.innerText = "player2가 승리했습니다!"
    p2count += 1
    countB.innerText = p2count
  }
  else{
    modalContent.innerText = "player1이 승리했습니다!"
    p1count += 1
    countA.innerText = p1count
  }
}

scissorButton.addEventListener("click", function() { totalRoatate(2)})
paperButton.addEventListener("click", function() { totalRoatate(0)})
rockButton.addEventListener("click", function() { totalRoatate(1)})