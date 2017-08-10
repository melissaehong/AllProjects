// ###Parens Valid
// Create a function that, given an input string `str`, returns a boolean whether parentheses in str are valid. Valid sets of parentheses always open before they close, for example. For `"Y(3(p)p(3)r)s"`, return `true`. Given `"N(0(p)3"`, return `false`: not every parenthesis is closed. Given `"N(0)t )0(k"`, return `false`.

// Track nest level: always >= 0; end as 0
function parensValid(str) {
    var numParens = 0;
    for (var idx = 0; idx < str.length; idx++) {
        if (str[idx] == "(") {
            numParens++;
        }
        if (str[idx] == ")") {
            numParens--;
        }
        if (numParens < 0) {
            return false;
        }
    }
    // Return an expression that evaluates to true/false
    return (numParens === 0);
}
