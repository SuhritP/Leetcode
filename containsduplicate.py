class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupNums = {}
        for i in nums:
            if i not in dupNums:
                dupNums[i] = i
            else:
                return True
        return False 

# the basic idea here is to find the duplicate number, used a hashmap to keep track of the numbers and add it to the map if not found
# the loop would eventually try to check for all numbers and when it encounters a duplicate the if else would trigger the else 
# and the program outputs true. The T.C is O(N) as a single loop is used and the S.C is O(N) as we use a map