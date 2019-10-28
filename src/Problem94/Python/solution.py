class Solution():
    def plusOne(self, digits):
        length = len(digits)

        # add 1 to last digit and carry
        digits[length-1] += 1
        carry = digits[length-1] / 10
        digits[length-1] %= 10

        # start adding from second to last
        for i in range(length-2, -1, -1):
            if carry == 1:
                digits[i] += 1
                carry = digits[i] / 10
                digits[i] %= 10
        if carry == 1: # if the last digit was 9, add 1 to the front
            digits.insert(0,1)
        return digits
num = [9, 9, 9]
print(Solution().plusOne(num))
# [1, 0, 0, 0]