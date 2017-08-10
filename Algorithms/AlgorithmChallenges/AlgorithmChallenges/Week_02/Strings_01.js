// Remove blanks
// Create a function that, given a string, returns a string without blanks. Given `" play that Funky Music "`, returns a string containing `"playthatFunkyMusic"`.

function removeBlanks(str) {
    var strToReturn = ''

    for (var i = 0; i < str.length; i += 1) {
        if (str[i] !== " ") {
            strToReturn += str[i];
        }
    }
    return strToReturn;
}

// Or take advantage of split and join!

function removeBlanks2(str) {
    return str.split(" ").join("");
}

// Acronyms
// Create a function that, given a string, returns the string’s acronym (first letters only, capitalized). Given `" there's no free lunch - gotta pay yer way. "`, return `"TNFL-GPYW"`. Given `"Live from New York, it's Saturday Night!"`, return `"LFNYISN"`.
function acronym(str) {
    var returnStr = "",
        // The next is initial variable will help us decide whether we want to add the letter to returnStr
        nextIsInitial = true;
    for (var idx = 0; idx < str.length; idx+=1) {
        if (str[idx] === " ") {
            nextIsInitial = true;
            continue;
        }
        // If it's not a space, check to see if it should be added to returnStr
        if (nextIsInitial) {
            nextIsInitial = false;
            returnStr += str[idx];
        }
    }
    return returnStr.toUpperCase();
}
