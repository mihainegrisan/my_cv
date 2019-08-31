let userScore = 0;
let computerScore = 0;
// Caching the DOM !
// variables that store DOM elements
const userScore_span = document.getElementById("user-score")
const computerScore_span = document.getElementById("computer-score")
const scoreBoard_div = document.querySelector(".score-board")
const result_p = document.querySelector(".result > p")
const rock_div = document.getElementById("r")
const paper_div = document.getElementById("p")
const scissors_div = document.getElementById("s")
const action_message_p = document.getElementById("action-message")

function getComputerChoice() {
    const choices = ['r', 'p', 's'];
    randomNumber = Math.floor(Math.random() * 3)
    return choices[randomNumber]
}

function convertToWord(letter) {
    if (letter === 'r') return 'Rock';
    if (letter === 'p') return 'Paper';
    return 'Scissors'
}

function win(userChoice, computerChoice) {
    const userChoice_div = document.getElementById(userChoice)
    userScore++;
    userScore_span.innerHTML = userScore;
    result_p.innerHTML = `${convertToWord(userChoice)}(user) beats  ${convertToWord(computerChoice)}(comp). You win!`;

    // GLOW
    userChoice_div.classList.add('green-glow');
    scoreBoard_div.classList.add('green-glow');
    // ES6
    setTimeout(() => userChoice_div.classList.remove('green-glow'), 300);
    // ES5
    setTimeout(function() { scoreBoard_div.classList.remove('green-glow') }, 300);
}

function lose(userChoice, computerChoice) {
    const userChoice_div = document.getElementById(userChoice)
    computerScore++;
    computerScore_span.innerHTML = computerScore;
    result_p.innerHTML = `${convertToWord(computerChoice)}(comp) beats  ${convertToWord(userChoice)}(user). You lose!`;
    userChoice_div.classList.add('red-glow');
    scoreBoard_div.classList.add('red-glow');
    setTimeout(() => userChoice_div.classList.remove('red-glow'), 300);
    setTimeout(() => scoreBoard_div.classList.remove('red-glow'), 300);

}

function draw(userChoice) {
    const userChoice_div = document.getElementById(userChoice)
    result_p.innerHTML = `It's a draw!`;
    userChoice_div.classList.add('grey-glow');
    scoreBoard_div.classList.add('grey-glow');
    setTimeout(() => userChoice_div.classList.remove('grey-glow'), 300);
    setTimeout(() => scoreBoard_div.classList.remove('grey-glow'), 300);
}

function game(userChoice) {
    action_message_p.style.visibility = 'hidden';
    const computerChoice = getComputerChoice();
    switch (userChoice + computerChoice) {
        case 'rs':
        case 'pr':
        case 'sp':
            win(userChoice, computerChoice);
            break;
        case 'rp':
        case 'ps':
        case 'sr':
            lose(userChoice, computerChoice);
            break;
        case 'rr':
        case 'pp':
        case 'ss':
            draw(userChoice);
            break;
    }
}

// adding event listeners to each button(picture)
function main() {
    rock_div.addEventListener('click', () => game("r"));
    paper_div.addEventListener('click', () => game("p"));
    scissors_div.addEventListener('click', () => game("s"));
}

main()
