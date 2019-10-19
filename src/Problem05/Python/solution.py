class Solution:
    def getRange(self, arr, target):
        try:
            targtIndex = arr.index(target)
        except ValueError:
            return [-1, -1]
        sol = [targtIndex]
        while target in arr[targtIndex+1:]:
            targtIndex += 1
        sol.append(targtIndex)
        return sol
        
# This solution runs in 0(n)

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]

arr = [1, 2, 3, 4, 5, 6, 7] 
x = 7
print(Solution().getRange(arr, x))
# [6, 6]

arr = [100, 150, 150, 153] 
x = 150
print(Solution().getRange(arr, x))
# [1, 2]

arr = [1, 2, 3, 4, 5, 6, 10] 
x = 9
print(Solution().getRange(arr, x))
# [-1, -1]
