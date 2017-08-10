// Reverse array
// Given a numerical array, reverse the order of the values. The reversed array should have the same length, with existing elements moved to other indices so that the order of elements is reversed.
// + BONUS: Don’t use a second array – move the values around within the array that you are given.

function reverseArr(arr) {
    //	Iterate halfway through array, swapping the value with the corresponding value in the other half of the array
    for (var i = 0; i < arr.length / 2; i += 1) {
        //	Make the swap w/ a temp variable
        var temp = arr[i];

        // 'arr.length - (i + 1)' just gives us the idx that's the same distance from the right edge as i is from the left edge.
        arr[i] = arr[arr.length - (i + 1)];
        arr[arr.length - (i + 1)] = temp;
    }

    return arr;
}

// Array Min to Front
// Given an array of comparable values, move the lowest element to the array’s front, shifting backward elements that previously were ahead of it. Change `[4,2,1,3,5]` to `[1,4,2,3,5]`.

function minToFront(arr) {
    // First find the lowest val/idx in array and record the index in variable
    var minIdx = 0,
        minVal;

    // Iterate through array once to find minIdx
    for (var i = 1; i < arr.length; i += 1) {
        if (arr[i] < arr[minIdx]) {
            minIdx = i;
        }
    }
    // Capture min value before it gets overwritten
    minVal = arr[minIdx];

    // Shift values to the right up through the index that originally held the minVal
    for (var i = minIdx; i > 0; i -= 1) {
        arr[i] = arr[i - 1];
    }

    // Overwrite 0th bucket with min value
    arr[0] = minVal;

    return arr;
}
