class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

# basically using the prefix sum helps in this question, start by setting the res list to default value
# which is 1 here and then make it the length of the nums list, then we can get the prefix for each 
# index in the res, the first one would be equated to the prefix which is 1 as there is nothing on the 
# left and the next ones are going to continue until we reach the end and do the same for the postfix
# and the res list is populated and we return it, the T.C is O(n) as we just have for loops and the 
# S.C is O(n) for the res list
        
        