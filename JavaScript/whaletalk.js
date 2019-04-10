/*
Project from Codecademy Javascript Course

There are a few simple rules for translating text to whale language:

- There are no consonants. Only vowels excluding “y”.
- The u‘s and e‘s are extra long, so we must double them in our program.

Once we have converted text to the whale language, the result is sung slowly, as is a custom in the ocean.
*/

let input = 'Teach me how you whale talk';
const vowels = ['a','e','i','o','u'];

let resultArray =[];

for(let i = 0; i < input.length;i++){
  for(let j = 0; j< vowels.length; j++)
  	if(input[i] === vowels[j]){
      resultArray.push(input[i]);
      if(input[i] === 'e' || input[i] === 'u'){
          resultArray.push(input[i]);
      }
    }
}
console.log(resultArray.join('').toUpperCase());
