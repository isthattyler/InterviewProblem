class Solution:
    def find_fixed_point(self, nums):
        length = len(nums)
        for i in range(length):
            numb = nums[i]
            if i == numb:
                return numb
        return None
arr = [-5, 1, 3, 4]
solution = Solution().find_fixed_point(arr)
print(solution)
