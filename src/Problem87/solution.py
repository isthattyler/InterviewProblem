def find_continuous(array, k):
    # use first number as first 
    start_sum = array[0]
    start_pos = 0

    candidate = [array[0]]

    index = 1
    size = len(array)
    while index <= size:
        # if total sum is larger than the target
        while start_sum > k:
            start_sum = start_sum - array[start_pos]
            candidate.pop(0)
            start_pos += 1
        if start_sum == k:
            return candidate
        start_sum += array[index]
        candidate.append(array[index])
        index += 1
        
print(find_continuous([1,3,2,5,7,2], 14))

## This runs in O(n)