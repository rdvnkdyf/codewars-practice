function getMostFrequent(json) {
  const temperatureData = json.temperature;
  const result = [];

  for (const dayTemperatures of temperatureData) {
    const frequencyMap = new Map();
    let mostFrequentValue = null;
    let maxFrequency = 0;
    let lastSeenIndex = -1;

    for (let i = 0; i < dayTemperatures.length; i++) {
      const temp = dayTemperatures[i];
      frequencyMap.set(temp, (frequencyMap.get(temp) || 0) + 1);

      const currentFrequency = frequencyMap.get(temp);

      if (currentFrequency > maxFrequency) {
        maxFrequency = currentFrequency;
        mostFrequentValue = temp;
        lastSeenIndex = i;
      } else if (currentFrequency === maxFrequency) {
        
      }
    }

    // After first pass, we know maxFrequency.
    // Now, find all values that have this maxFrequency.
    const candidates = [];
    for (const [temp, freq] of frequencyMap.entries()) {
      if (freq === maxFrequency) {
        candidates.push(temp);
      }
    }

    // Among candidates, find the one that appears latest.
    let finalMostFrequent = null;
    let latestIndex = -1;

    for (const candidate of candidates) {
      // Find the last index of this candidate
      const currentCandidateLastIndex = dayTemperatures.lastIndexOf(candidate);
      if (currentCandidateLastIndex > latestIndex) {
        latestIndex = currentCandidateLastIndex;
        finalMostFrequent = candidate;
      }
    }
    result.push(finalMostFrequent);
  }
  return result;
}