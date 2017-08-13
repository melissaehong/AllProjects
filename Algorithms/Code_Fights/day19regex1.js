function isSentenceCorrect(sentence) {
  var re = /^[A-Z][^.?!]*[.?!]$/;
  return console.log(re.test(sentence));
}

isSentenceCorrect('My name is Melissa!')
