class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charSet1 = {}
        charSet2 = {}
        if (len(s) != len(t)):
            return False

        for i in s:
            if i in charSet1:
                charSet1[i] += 1
            else:
                charSet1[i] = 1
        for i in t:
            if i in charSet2:
                charSet2[i] += 1
            else:
                charSet2[i] = 1
        
        return charSet1 == charSet2

#anagram is if its the same word but thr letters are arranged differently, so the first thing would be to check if the lengths are equal
#if not we return false and then we create two maps for each string and then check if the maps are equal if not then we get false or else true
# the maps have to be equal for valid anagram as the letters and frequencies of an anagram are the same