function nextItem(xs, item) {
    // A flag to indicate if we have found the item.
    let found = false;

    // Iterate through each element in the sequence.
    for (const x of xs) {
        // If the flag is true, it means the current element 'x' is the one
        // we are looking for (the one after our target). Return it.
        if (found) {
            return x;
        }

        // If the current element 'x' matches the target 'item',
        // set the 'found' flag to true. The next iteration will then return the next item.
        if (x === item) {
            found = true;
        }
    }

    // If the loop finishes without returning, it means either the item was not found,
    // or it was the last item in the sequence. In both cases, there's no "next" item.
    return undefined;
}