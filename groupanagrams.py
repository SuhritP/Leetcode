class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]
        return list(res.values())
        

# the basic idea of the code is to use a map with each letter in the alpha bet with a key value pair like with ['abc'] str the key would be [0: 1, 1: 1, 2: 1] etc 
# as each key is the ord value and it maps to the freq, we use ord here as for chars we subtract the default of a and anything left after would be the correspoding 
# letter, we then check if the key and we do tuple as its immuatable and we check if its in res if yes we append that and if not we map it to a string of list and return
# the list of the res.values