// Is Palindrome

// Create a function that, given an input string, returns a boolean whether the string is a palindrome (mirrored from beginning to end). Given "abba" or "racecar", return true. Given "Non", return false.

//  Compare from both sides toward center.
//  Fast-fail if inequal, else success.

function isPalindrome(str) {
    for (var idx = str.length - 1; idx >= str.length / 2; idx -= 1) {
        if (str[idx] != str[str.length - 1 - idx]) {
            return false;
        }
    }
    return true;
}

// In order to ignore white space (spaces, tabs, returns), capitalization and punctuation, let's shift to a while loop and pull in regex.

function isPalindromeBonus(str) {
  // Regex pattern to capture punctuation and white spice
  var regexPattern = /[.,\/#!$%\^&\*;:{}=\-_`~()\?\s]/,
      rightEdge = str.length - 1,
      leftEdge = 0,
      validCharExists = false;

  while ( rightEdge >= leftEdge ) {
    // Scoot the edges over if they encounter a character to ignore
    if ( regexPattern.test(str[rightEdge]) ) {
      rightEdge -= 1;
      continue;
    }

    if ( regexPattern.test(str[leftEdge]) ) {
      leftEdge += 1;
      continue;
    }

    validCharExists = true;

    // If we're here, it's not a character to ignore, so test equality (ignoring case). Return false if unequal.
    if ( str[rightEdge].toUpperCase() !== str[leftEdge].toUpperCase() ) {
      return false;
    }
    // If here, the characters were valid and equal; shift them toward eachother.
    leftEdge += 1;
    rightEdge -= 1;
  }
  return validCharExists;
}
