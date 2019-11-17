# this solution uses recursion
def permute(nums):
    if not nums: # if empty
        return []
    length = len(nums)
    if length == 1: # if there's one item, permutation is itself
        return [nums]
    sol = []
    for i in range(length):
        temp = nums[i]
        # remove i from nums
        remaining = nums[:i] + nums[i+1:]
        for j in permute(remaining):
            sol.append([temp] + j)
    return sol

print(permute([1, 2, 3]))
# [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]
