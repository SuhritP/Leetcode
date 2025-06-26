class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergeStr = ""
        if (len(word1) > len(word2)):
            for i in range(len(word2)):
                mergeStr+= word1[i] + word2[i]
            mergeStr += word1[i + 1: len(word1)]
        else:
            for j in range(len(word1)):
                mergeStr+= word1[j] + word2[j]
            mergeStr += word2[j + 1: len(word2)]
        return mergeStr



# identify the longer string and shorter string and based on which is longer, loop through the shorter till the end to merge and then add the 
# remaining string back to the merged. The T.C is O(N) as there is a for loop and S.C is O(N) because of the mergeStr 