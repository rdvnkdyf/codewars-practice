package kata

import (
	"fmt"
	"strings"
)

func countSheep(num int) string {
	if num == 0 {
		return ""
	}

	var sb strings.Builder
	for i := 1; i <= num; i++ {
		sb.WriteString(fmt.Sprintf("%d sheep...", i))
	}

	return sb.String()
}