def two_sum(lst, k):
    seen = []

    for i in lst:
        num = k - i
        if num in seen:
            return True
        seen.append(i)
    return False

print(two_sum([4, 7, 1, -3, 2], 5))
