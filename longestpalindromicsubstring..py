#brute force solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = ""
        length = len(s)
        for i in range(length - 1, -1, -1):
            rev = rev + s[i]
        if (s == rev):
            return True
        return False

    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or self.isPalindrome(s):
            return s
        longest_str = s[0]  
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                substring = s[i:j+1]            
                if self.isPalindrome(substring) and len(substring) > len(longest_str):
                    longest_str = substring
        return longest_str


# O(N^3) solution, its because isPalindrome is O(N) and finding each substring is O(N^2), the helper function checks if its a palindrome
# the longest palindrome function works by first populating all the substrings and then checking it if its a palindrome or not and updates
# the longest_str accordingly, the space complexity is O(N) as although I am creating a lot of substrings, they are not being stored 
#permanently which saves the space and the maximum space take is O(N)


#optimal solution

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        longPal = s[0]

        for i in range(len(s)):
            l,r = i,i
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                if (r - l + 1) > longest:
                    longPal = s[l:r+1]
                    longest = len(longPal)
                l -= 1
                r += 1
 
        for i in range(len(s)):
            l,r = i,i+1
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                if (r - l + 1 ) > longest:
                    longPal = s[l:r+1]
                    longest = len(longPal)
                l -= 1
                r += 1

        return longPal


# the basic idea is that you first start from the center and then keep expanding from there by incrementing the right pointer and decrementing
# the left pointer, we check the conditions that the left >=0 and right < len(s) and also check if left and right character is equal and 
# only if the indices are greater than the longest we update the longest to reflect that, for even as there is no symmetry we can just make
# sure to start the right one to the right of left. The basic overall idea would be for a string babad, it would go to b and see that
# there is no left and thus it goes to the next after the first update from the while loop and once it reaches a it goes it the while loop
# and then both the left and right point to b at 0 index and 3 index due to the increment and decrement and longestPal is updated