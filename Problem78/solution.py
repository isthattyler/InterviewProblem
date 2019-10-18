class Solution(object):
    def findSingle(self, nums):
        seen = []
        size = len(nums)

        for i in range(size):
            num = nums[i]
            if num in seen:
                seen.remove(num)
            else:
                seen.append(num)
        return seen.pop()

nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
print(Solution().findSingle(nums))