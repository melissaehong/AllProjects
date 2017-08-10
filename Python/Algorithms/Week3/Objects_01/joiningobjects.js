function innerJoin(users, books, usersHaveBooks){
var newArr = [];
var recordIdx = 0;
console.log(users, usersHaveBooks, books);
for (var recordIdx = 0; recordIdx < usersHaveBooks.length; recordIdx +=1){
  var miniArr = [];
  //need obj from usersHavebooks
  //need obj from users
  //need obj from books
  var usersHaveBooksObj = usersHaveBooks[recordIdx];
  miniArr.push(usersHaveBooksObj);
  for (var userIdx = 0; userIdx < users.length; userIdx += 1){
    if (usersHaveBooksObj.user_id === users[userIdx].id){
      miniArr.push(users[userIdx]);
      break;
    }
  }
}
for (var bookIdx = 0; bookIdx < books.length; bookIdx += 1){
  if (usersHaveBooksObj.book_id === books[bookIdx].id){
    miniArr.push(books[bookIdx]);
    break;
  }
}
newArr.push(miniArr);

return newArr;
}

/*function leftJoin(arr1, arr2, arr3){
  if(arr1.first_name){

  } else if (arr1.book_title){

  } else if {

 var arrToReturn = [];

 for (var arr1Idx = 0; arr1Idx <arr1.length; arr1Idx += 1){
   var miniArr = [];
   miniArr.push(arr1[arr1Idx]);
 }
}
}*/
