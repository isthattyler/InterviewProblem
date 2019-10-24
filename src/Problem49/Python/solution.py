class Solution:
    def sortColors(self, nums):
        front = 0
        length = len(nums) - 1
        index = 0
        while index <= length:
            if nums[index] == 0: # move 0 to lower left
                nums[front], nums[index] = nums[index], nums[front]
                front += 1
                index += 1
            elif nums[index] == 2: # move 2 to upper right
                nums[index], nums[length] = nums[length], nums[index]
                length -= 1
            else:
                index += 1
        return nums

nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

Solution().sortColors(nums)
print("After Sort: ")
print(nums)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]