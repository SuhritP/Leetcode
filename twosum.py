class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    lst.append(i)
                    lst.append(j)
        return lst


# super brute force solution, used the classic double loop structure with a T.C of O(N^2) and S.C of O(1)

#approach 2: map

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[num] = i
        return


# use a map, start by calculating the differences between an element and the target and check if its 
# in the map, if yes, then return the current index and the value to the index, here keys are the 
# elements from the list and if we don't find the diff then we just add it with the key being the
# list elements and the values being the indexes 