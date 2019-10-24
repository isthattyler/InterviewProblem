class Solution(object):
    def compress(self, chars):
        temp = chars[0]
        count = 0
        sol = []
        for i in chars:
            if not (temp == i):
                sol.append(temp)
                if not (count == 1): # don't add 1 occurence
                    sol.append(count) 
                temp = i # set new variables
                count = 1
            else:
                count += 1
        # add the last element and its occurence
        sol.append(temp)
        if not (count == 1):
            sol.append(count)
        return sol
                

print(Solution().compress(['a', 'a', 'b', 'c', 'c', 'c', 'd']))
# ['a', '2', 'b', 'c', '3', 'd']