function sakuraFall(v) {
  // If the initial velocity is non-positive, the return value should be 0.
  if (v <= 0) {
    return 0;
  }

  // The total distance (height of the branch) is constant.
  // We know that at 5 cm/s, it takes 80 seconds to reach the ground.
  // Distance = Speed × Time
  const distance = 5 * 80; // This calculates to 400 cm

  // Now, calculate the time it takes for a petal with speed 'v' to fall the same distance.
  // Time = Distance / Speed
  const time = distance / v;

  return time;
}