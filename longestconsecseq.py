class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num = set(nums)
        for i in num:
            if i - 1 not in num:
                length = 0
                while (i + length) in num:
                    length += 1
                longest = max(length, longest)
        return longest

# Took some time to understand, implementation was straightforward, basically you use a set and not a map 
# or a list as when we find the element in the set its O(1) T.C as map and list are sorted while set is unsorted 
# we also dont really need to keep track of indices, the basic logic is to check if the number before that element is
# in the set and if not we start looping through the next element in the seqenece and update the variable longest 
# accordingly, if there is a previous element we do nothing. Now the reason why it's not O(N^2) is because each while 
# only checks for the cases of i - 1 being present and even in worst case with the longest sequence the check happens 
# only once so that's why T.C is O(N), S.C is O(N) because of the set