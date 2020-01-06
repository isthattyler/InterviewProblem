def is_shifted(str1, str2):
    if str1 == str2:
        return True
    if (not str1 or not str2) or (not len(str1) == len(str2)):
        return False
    temp = str1 + str1 # concat string str1 twice
    if (temp.count(str2) > 0): # check number of occurence in temp substring
        return True

print(is_shifted('abcde', 'cdeab'))
# True

# The function runs in O(size(str1)+size(str2))
