package kata

import (
  "sync"
)

// Merge takes two read-only string channels and returns a single read-only string channel
// that receives all messages from both input channels. The returned channel is closed
// once both input channels are closed.
func Merge(a <-chan string, b <-chan string) <-chan string {
  // Create an output channel.
  out := make(chan string)
  
  // Use a WaitGroup to wait for all goroutines to finish.
  var wg sync.WaitGroup
  
  // Add two goroutines to the WaitGroup, one for each input channel.
  wg.Add(2)
  
  // Start a goroutine to read from channel 'a' and send to 'out'.
  go func() {
    // When the goroutine finishes, signal the WaitGroup.
    defer wg.Done()
    for v := range a {
      out <- v
    }
  }()
  
  // Start a goroutine to read from channel 'b' and send to 'out'.
  go func() {
    // When the goroutine finishes, signal the WaitGroup.
    defer wg.Done()
    for v := range b {
      out <- v
    }
  }()
  
  // Start another goroutine to close the output channel after all
  // the other goroutines are done.
  go func() {
    // Wait for both message-forwarding goroutines to complete.
    wg.Wait()
    // Close the output channel.
    close(out)
  }()
  
  // Return the merged channel.
  return out
}