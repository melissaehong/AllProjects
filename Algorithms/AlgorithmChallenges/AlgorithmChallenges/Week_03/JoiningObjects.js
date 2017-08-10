function innerJoin() {
    // Create array to return
    var arrToReturn = [];

    // Loop over usersHaveBooks
    for (var recordIdx = 0; recordIdx < usersHaveBooks.length; recordIdx += 1) {
        // Creating miniArr that will hold record obj, userobj, and bookobj
        // initially just put the record obj we have access to inside
        var miniArr = [usersHaveBooks[recordIdx]]

        // Find correct user object
        var correctUserObj = findById(usersHaveBooks[recordIdx].user_id, users)

        // Find correct book object
        var correctBookObj = findById(usersHaveBooks[recordIdx].book_id, books)

        // Put user obj in miniArr
        miniArr.push(correctUserObj)
            // Put book obj in miniArr
        miniArr.push(correctBookObj)

        // ALTERNATE CODE CAN TAKE PLACE OF EVERYTHING ABOVE
        // var miniArr = [usersHaveBooks[recordIdx],findById(usersHaveBooks[recordIdx].user_id, users),findById(usersHaveBooks[recordIdx].book_id, books)];

        // If we're here, miniArr is completed and we can add to arrToReturn
        arrToReturn.push(miniArr)
    }

    return arrToReturn
}

function findById(providedId, records) {
    // Use the id passed in to find the matching object in record
    for (var searchIdx = 0; searchIdx < records.length; searchIdx += 1) {
        if (records[searchIdx].id === providedId) {
            return records[searchIdx];
        }
    }
    // If we get here, no record with providedId as id property
    return {
        error: "No record found"
    }

}
