let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:
function generateTarget() {
    return Math.floor(Math.random(0, 10));
};

function compareGuesses(hguess, cguess, sguess) {
    alertMessage(hguess);
    const hresult = getAbsoluteDistance(hguess, sguess);
    const cresult = getAbsoluteDistance(cguess, sguess);
    if (hresult < cresult) {
        return true;
    } else if (cresult < hresult) {
        return false;
    } else {
        return true;
    }
};
function updateScore(winner) {
    if (winner === "human") {
        humanScore++;
    } computerScore++;
};
function advanceRound() {
    currentRoundNumber++;
}
function getAbsoluteDistance(num1, num2) {
    return Math.abs(num1 - num2);
}

function alertMessage(userGuess) {
    if (userGuess > 9 || userGuess < 0) {
        alert('Guess not in range!, Guess must be between 1 and 10.');
    }
};

