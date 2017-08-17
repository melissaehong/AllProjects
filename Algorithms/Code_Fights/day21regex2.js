function swapAdjacentWords(s) {
  return s.replace(/(\w+)\s(\w+)/g, "$2 $1");
}
               
