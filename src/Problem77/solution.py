## implement using recursion

class Solution(object):
    def fibonacci(self, n):
        if n <= 1:
            return n
        return self.fibonacci(n-1) + self.fibonacci(n-2)

n = 9
print(Solution().fibonacci(n))
