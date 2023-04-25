// 코드를 작성해 주세요
const scissorsButton = document.getElementById('scissors-button')
const rockButton = document.getElementById('rock-button')
const paperButton = document.getElementById('paper-button')
const modal = document.querySelector('.modal')
const modalContent = document.querySelector('.modal-content')
const player1Img = document.querySelector('#player1-img')
const player2Img = document.querySelector('#player2-img')

modal.addEventListener('click', () => modal.style.display = 'none')

let count1 = 0
let count2 = 0

const playGame = (p1Choice, p2Choice) => {
  switch (p1Choice) {
    case 'rock':
      switch (p2Choice) {
        case 'rock': 
        return 0
        case 'paper':
          return 2
        case 'scissors':
          return 1
      }
    case 'paper':
      switch (p2Choice) {
        case 'rock': 
          return 1
        case 'paper':
          return 0
        case 'scissors':
          return 2
      }
    case 'scissors':
      switch (p2Choice) {
        case 'rock': 
          return 2
        case 'paper':
          return 1
        case 'scissors':
          return 0
      }
  }
}

const choiceButton = function (choice) {
  return () => {
        // 각 버튼에 마우스와 관련된 모든 이벤트를 제거하는 속성을 추가합니다.
    scissorsButton.setAttribute('disabled', 'true')
    scissorsButton.setAttribute('style', 'pointer-events: none;')
    rockButton.setAttribute('disabled', 'true')
    rockButton.setAttribute('style', 'pointer-events: none;')
    paperButton.setAttribute('disabled', 'true')
    paperButton.setAttribute('style', 'pointer-events: none;')
    
    const cases = ['scissors', 'rock', 'paper']
    const randomChoice = cases[Math.floor(Math.random() * 3)]
    
    const result = playGame(choice, randomChoice)
    if (result === 1) {
      count1 += 1
    } else if (result === 2) {
      count2 += 1
    }

    player1Img.src = `img/${choice}.png`

    let i = 0
    const randomImg = setInterval(() => {
      i = (i + 1) % 3
      player2Img.src = `img/${cases[i]}.png`
    }, 100)

    setTimeout(() => {
      clearInterval(randomImg)
      const countA = document.querySelector('.countA')
      const countB = document.querySelector('.countB')
      countA.innerText = count1
      countB.innerText = count2
      
      player2Img.src = `img/${randomChoice}.png`
      
      modalContent.innerText = result ? `player${result} 의 승리입니다!` : '무승부입니다!'
      modal.style.display = 'flex'
        
      scissorsButton.removeAttribute('disabled')
      scissorsButton.removeAttribute('style')
      rockButton.removeAttribute('disabled')
      rockButton.removeAttribute('style')
      paperButton.removeAttribute('disabled')
      paperButton.removeAttribute('style')
    }, 3000)
  }
}

scissorsButton.addEventListener('click', choiceButton('scissors'))
rockButton.addEventListener('click', choiceButton('rock'))
paperButton.addEventListener('click', choiceButton('paper'))