def singleNumber(nums):
    sol = []
    for i in nums:
        if i not in sol:
            sol.append(i)
        else:
            sol.remove(i)
    return sol.pop()

# This solution runs in O(n) time
print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1
