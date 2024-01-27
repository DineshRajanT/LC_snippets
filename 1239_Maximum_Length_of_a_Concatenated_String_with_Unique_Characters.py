from collections import Counter
from typing import List, Set

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # T: O(2^n)
        # S: O(n)

        def backtracking(i: int, charSet: Set[str]) -> int:
            if i == len(arr):
                return len(charSet)
            
            newString = arr[i]
            maxLength = 0

            # Option 1: Include the new string (if it's unique)
            if isUnique(charSet, newString):
                    newSet = set(charSet)
                    for c in newString:
                        newSet.add(c)
                    maxLength = backtracking(i + 1, newSet)
        
            # Option 2: Don't include the new string
            return max(maxLength, backtracking(i + 1, charSet))
        
        def isUnique(charSet: Set[str], newString: str) -> bool:
            count = Counter(charSet) + Counter(newString)
            return max(count.values()) == 1
    
        return backtracking(0, set())