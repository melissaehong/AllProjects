function multiply(array, value){
for (var i = 0; i<array.length-1; i++){
	array[i] = array[i] * value;
	}
return array;
}

debug(multiply([0,1,2], 4))