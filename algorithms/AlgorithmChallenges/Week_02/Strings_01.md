##Strings Day 1 ([Solutions](Strings_01.js))

Strings are arrays of characters (more accurately, you can read individual characters the same way you read specific values in a numerical array, and these individual values are strings of length 1). However, you cannot write individual characters in a string in this same way. Once a string is defined, individual characters can be referenced by [ ] but not changed. Strings are immutable: they can be completely replaced in their entirety, but not changed piecewise. To manipulate string characters, you must split the string to an array, make individual changes, then join it.

For the following, feel free to use any of the following built-in functions (not required though!): `split`, `join`, `concat` (look up how to use them in the [MDN Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript)).

###Remove blanks
Create a function that, given a string, returns a string without blanks. Given `" play that Funky Music "`, returns a string containing `"playthatFunkyMusic"`.

###Acronyms
Create a function that, given a string, returns the string’s acronym (first letters only, capitalized). Given `" there's no free lunch - gotta pay yer way. "`, return `"TNFL-GPYW"`. Given `"Live from New York, it's Saturday Night!"`, return `"LFNYISN"`. The built-in `toUpperCase` method might be useful here...
