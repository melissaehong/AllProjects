// Most Repeated Character
// Given a string, `return` the character that's used most often, along with the number of times it's repeated.

function mostRepeatedChar(str){
  var charCounter = {},
      maxChar = {
        letter: null,
        times: null
      }
  // Build up a dictionary of word counts and keep track of max
  for (var i = 0; i < str.length; i += 1) {
    if( charCounter[str[i]] ) {
      charCounter[str[i]] += 1;
    } else {
      charCounter[str[i]] = 1;
    }
    // Now check to see if it should be the max!
    if (charCounter[str[i]] > maxChar.times) {
      maxChar.letter = str[i];
      maxChar.times = charCounter[str[i]];
    }
  }

  return maxChar;
}
