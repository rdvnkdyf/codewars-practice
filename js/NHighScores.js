function topScores(records, nTop) {
  // Edge case: if nTop is negative or 0, return an empty list immediately.
  if (nTop <= 0) {
    return [];
  }

  // Use a Map to store the highest score for each player.
  // A Map is efficient for key-value pairs (player name -> highest score).
  const highestScores = new Map();

  // Iterate through the records to find the highest score for each player.
  for (const [name, score] of records) {
    // Check if the player is already in the map.
    // If not, or if the current score is higher than the existing one, update the map.
    if (!highestScores.has(name) || score > highestScores.get(name)) {
      highestScores.set(name, score);
    }
  }

  // Convert the Map entries into an array of [name, score] pairs.
  const uniquePlayers = Array.from(highestScores.entries());

  // Sort the unique players array based on the rules:
  // 1. Sort by score in descending order (highest to lowest).
  // 2. If scores are equal, sort by name in ascending alphabetical order.
  uniquePlayers.sort((a, b) => {
    const scoreA = a[1];
    const scoreB = b[1];
    const nameA = a[0];
    const nameB = b[0];

    // Primary sort: by score, descending
    if (scoreA !== scoreB) {
      return scoreB - scoreA;
    }

    // Secondary sort: by name, ascending (if scores are the same)
    return nameA.localeCompare(nameB);
  });

  // Slice the sorted array to get only the top nTop records.
  // This also handles the case where nTop is greater than the number of unique players,
  // as slice will just return all available elements.
  return uniquePlayers.slice(0, nTop);
}