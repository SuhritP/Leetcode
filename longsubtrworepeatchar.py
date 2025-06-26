class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res


# okay so the basic idea of the code is to use the sliding window technique which adds a character to the set if not
# found and it keeps doing that, once a character is found it removes the left most character until its not found and 
# updates the left pointer, with that the max res can be calculated, for example for pwwkew, we start with p and then add
# to the set, then with w and once we reach the second w, it removes p first and then goes to w and remvoes that, again
# we use set here for simple look ups and not maps as we dont really need any order just fast look up
# T.C is O(N) even though its two nested loops as the while doesn't run for every check and the program removes and adds
# each element at most once S.C is O(N) because of the set