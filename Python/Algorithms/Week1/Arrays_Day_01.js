//Push Front

function push_front(arr, value){
	for (var i=arr.length; i > 0; i -= 1) {
	arr[i] = arr[i-1];
	}
	arr[0] = value;
	return arr;
	}

/* function pushFront(arr, value){
Solution #1
 Create a new array with value in first position
  var newArr = [value];
 Iterate through given array, pushing vals in order
  for ( var idx = 0; idx < arr.length; idx +=1){
  newArr.push(arr[idx]);
  }
 Return new array
  return newArr;
}

**however, this creates a new array**

console.log( pushFront([4,5,2,-18,21], 42) );

   [0, 1, 2, 3, 4], -1 => [-1, 0, 1, 2, 3, 4]

Solution #2
function pushFront2(arr, value){
Iterate through the array from the end
  for (var i = arr.length; i > 0; i--){
	console.log(arr[i]);
  }

variables | values
------------------
arr       | [0,1,2,3,4]
value     | -1
i         | 5
arr[i]    | undefined

output:
1. undefined
2. 4
3. 3
4. 2
5. 1
6. undefined (because of no return)

As we move through the array, shift each value to the right
    arr[i] = arr[i-1];
  }
Once we're done looping, paste given value into 0 location
  	arr[0] = value
  	return arr;
*/

//Pop Front
//Given array, remove and return the value at the beginning of the array. Do this without using any built-in array methods except pop().

function pop_front(arr){
	arr.pop(arr(arr.length-1));
	for (var i=arr.length; i > 0; i-= 1) {
		arr[i] = arr[i-1];
	}
	arr[0] = arr(arr.length-1);
	return arr;
}



//Insert At
//Given array, index, and additional value, insert the value into array at given index. You can think of PushFront(arr,val) as equivalent to InsertAt(arr,0,val).

function insert_at(arr, index, value){
	for (var i=arr.length; i>index; i-=1){
		arr[i]=arr[i-1];
	}
	arr[index]=value;
	return arr;
}
