// Push Front
// Given array and an additional value, *insert this value* at the beginning of the array.

function pushFront(arr, value) {
    // Start from the end of the array, pushing everything back by one
    for (var i = arr.length; i > 0; i -= 1) {
        arr[i] = arr[i - 1];
    }
    // Now we can set the new value to position 0
    arr[0] = value;
    return arr;
}

// Pop Front
// Given array, *remove and return* the value at the beginning of the array. Do this without using any built-in array methods except `pop()`.

function popFront(arr) {
    // Store the first value in the array in a variable
    // Iterate through the array, pushing every value forward
    // Shorten the array by 1
    // Return the stored value

    var valToReturn = arr[0];

    for (var i = 0; i < arr.length; i += 1) {
        arr[i] = arr[i + 1];
    }

    arr.length = arr.length - 1;
    // Or you can use arr.pop();

    return valToReturn;
}

// Insert At
// Given array, index, and additional value, insert the value into array at given index. You can think of `PushFront(arr,val)` as equivalent to `InsertAt(arr,0,val)`.

function insertAt(arr, idx, value) {
    // Iterate from end of array, shifting values to the right, until reaching the idx
    // Replace arr[idx] with value
    for (var i = arr.length; i > idx; i -= 1) {
        arr[i] = arr[i - 1];
    }
    arr[idx] = value;
    return arr;
}
