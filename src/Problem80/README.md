# Problem 80: String Compression

This problem was recently asked by Twitter:

Given an array of characters with repeats, compress it in place. The length after compression should be less than or equal to the original array.

Example:

```bash
Input: ['a', 'a', 'b', 'c', 'c', 'c']
Output: ['a', '2', 'b', 'c', '3']
```

Here's a starting point:

```python
class Solution(object):
  def compress(self, chars):
    # Fill this in.

print Solution().compress(['a', 'a', 'b', 'c', 'c', 'c'])
# ['a', '2', 'b', 'c', '3']
```