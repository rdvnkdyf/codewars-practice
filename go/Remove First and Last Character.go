package kata

func RemoveChar(word string) string {
 if len(word) <= 2 {
        return ""
    }

    // Use string slicing to create a new string that starts at the second character (index 1)
    // and ends at the second-to-last character (index len(s)-1).
    // The syntax s[1:len(s)-1] includes the character at index 1 but excludes the one at len(s)-1.
    return word[1 : len(word)-1] 
}