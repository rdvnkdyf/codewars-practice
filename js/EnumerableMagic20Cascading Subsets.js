function eachCons(array, n) {
	// The result array to hold our subsets.
	const result = [];
	
	// Loop through the array up to the point where a full subset of size 'n' can still be formed.
	// This ensures we don't try to create a subset from fewer than 'n' elements.
	for (let i = 0; i <= array.length - n; i++) {
		// Use the slice() method to create a new array containing the elements from 'i' up to 'i + n'.
		// This creates the cascading subset.
		result.push(array.slice(i, i + n));
	}
	
	return result;
}