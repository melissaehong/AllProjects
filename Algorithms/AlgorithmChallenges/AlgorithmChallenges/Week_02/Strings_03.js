function bookIndex(pageArr) {
  // Set up the string to eventually return
  var indexStr = "",
      // This flag variable will tell us whether we're in a consecutive page range
      rangeStarted = false;

  // Iterate through array, asking whether it's consecutive to previous value and whether we've already started a range
  for (var arrIdx=1; arrIdx < pageArr.length; arrIdx+=1) {
    // Is page consecutive to prev one?
    if (pageArr[arrIdx] !== pageArr[arrIdx - 1] + 1) {
      // No, page not part of a range, reset flag as false
      rangeStarted = false;
      indexStr += pageArr[arrIdx-1] + ", ";

    } else {
      // Yes. Create new range or extend?
      if (!rangeStarted) {
        // Create new range
        rangeStarted = true;
        indexStr += pageArr[arrIdx-1] + "-";
      }
      // (If extending a range, do nothing, i.e. we don't add that page to string)
    }
  }
  // Add the final page w/out a comma
  indexStr += pageArr[pageArr.length - 1];
  return indexStr;
}
