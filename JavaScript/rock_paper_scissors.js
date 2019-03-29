const getUserChoice = userInput =>{
  userInput = userInput.toLowerCase();
  if(userInput === 'rock' || userInput === 'paper' || userInput === 'scissors' ||userInput === 'bomb'  ){
    return userInput;
  }else{
    console.log('Please enter rock, paper or scissors');
  }
};

const getComputerChoice =()=> {
  let choice =Math.floor(Math.random()*3);
  if(choice === 0){
    return 'rock';
  }else if(choice === 1){
    return 'scissors';
  }else{
    return 'paper';
  }
}

const determineWinner = (userChoice, computerChoice) => {
  
  if (userChoice === 'bomb'){
    return 'The user wins';
  }
  if(userChoice === computerChoice){
    return 'The game is a tie';
  }
  
  if(userChoice === 'rock'){
    if(computerChoice == 'paper'){
      return 'The computer wins';
    }else{
      return 'The user wins';
    }
    
  }
  
  if(userChoice === 'paper'){
    if(computerChoice == 'scissors'){
      return 'The computer wins';
    }else{
      return 'The user wins';
    }
  
  }
  
  if(userChoice === 'scissors'){
    if(computerChoice == 'rock'){
      return 'The computer wins';
    }else{
      return 'The user wins';
    }
  }
}

const playGame = ()=>{
  let userChoice = getUserChoice('bomb');
  console.log(userChoice);
	let computerChoice = getComputerChoice();
  console.log(computerChoice);
console.log(determineWinner(userChoice, computerChoice));
}

playGame();



