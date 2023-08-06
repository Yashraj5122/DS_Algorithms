from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)
        result = []

        for s in strs:
            sort_s = tuple(sorted(s))
            anagramMap[sort_s].append(s)

        for values in anagramMap.values():
            result.append(values)

        return result
