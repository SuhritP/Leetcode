class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        freq = {}
        max_freq = []
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        
        for i in range (k):
            max_key = max(freq, key=freq.get)
            max_freq.append(max_key)
            freq.pop(max_key)
        return max_freq

# the idea is to use a map with the element pointing to its freq, in python, unlike cpp, if the map
# doesnt point to anything, the value isnt 0, so we have specify the value using the get which 
# now defaults to 0 if not found, next we go through k and we try to find the max key for the freq
# and then add it to the list and pop it. for the max() function here, the default returns the max key
# so using the key = freq.get we are getting the values and we can then return the max key from there
# the T.C is O(n) for the first loop and O(k) for the second loop, so O(n+k) which is O(n)
#the space complexity is O(n) as we are using a map and returning a list



