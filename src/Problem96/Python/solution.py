class Solution(object):
    def topKFrequent(self, words, k):
        count = {}
        # O(N) time to count the array
        for key in words:
            if key not in count:
                count[key] = 1
            else:
                count[key] += 1
        # Fastest speed to sort is O(N.log(n)) in Python
        return [key for key in sorted(count, key=lambda x: (-count[x], x))[:k]]

# Overall, the function takes O(N.log(n)) to run
words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print(Solution().topKFrequent(words, k))
# ['pro', 'daily']
