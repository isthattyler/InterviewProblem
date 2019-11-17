# Problem 96: Top K Frequent words

This problem was recently asked by AirBNB:

Given a non-empty list of words, return the k most frequent words. The output should be sorted from highest to lowest frequency, and if two words have the same frequency, the word with lower alphabetical order comes first. Input will contain only lower-case letters.

Example:

```bash
Input: ["daily", "interview", "pro", "pro", 
"for", "daily", "pro", "problems"], k = 2
Output: ["pro", "daily"]
```

```python
class Solution(object):
  def topKFrequent(self, words, k):
    # Fill this in.

words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print(Solution().topKFrequent(words, k))
# ['pro', 'daily']
```