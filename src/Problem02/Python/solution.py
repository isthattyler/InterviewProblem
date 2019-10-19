class Solution:
    def lengthOfLongestSubstring(self, s):
        lengthSoFar = 0
        longestLength = 0
        seen = []

        for i in s:
            if i in seen:
                if longestLength <= lengthSoFar:
                    longestLength = lengthSoFar
                    lengthSoFar = 0 # reset counter after encounter a dup
                seen = [] # reset seen list after encounter a dup
            else:
                lengthSoFar += 1
                seen.append(i)
        return longestLength
print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))

# This solution runs in O(n) time.
# This solution is done with an assumption that there's always at least a repeating character in the string.
# If there's a case that no character is repeated, this solution needs to be adjusted.
# In the future I will add an extra solution to account for this case.