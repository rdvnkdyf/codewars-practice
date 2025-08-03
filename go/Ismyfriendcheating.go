package kata

func RemovNb(m uint64) [][2]uint64 {
    
    sumTotal := m * (m + 1) / 2

    
    target := sumTotal + 1

    var result [][2]uint64 // Slice to store the valid pairs [a, b]

   
    for a := uint64(1); a <= m; a++ {
        // We know (a+1)(b+1) = target
        // So, (b+1) = target / (a+1)
        
        // Check if (a+1) is a divisor of target
        if (a+1) > 0 && target%(a+1) == 0 {
            // Calculate b_plus_1
            bPlus1 := target / (a + 1)
            
            // Calculate b
            b := bPlus1 - 1

            
            if b >= 1 && b <= m {
                // Add the pair [a, b] to the result
                result = append(result, [2]uint64{a, b})
            }
        }
    }

    
    return result
}