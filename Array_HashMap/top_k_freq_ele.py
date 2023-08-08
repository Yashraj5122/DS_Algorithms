class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = {}

        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i]+=1
        
        freq_list = []

        for freq in dic.values():
            freq_list.append(freq)
        
        freq_list.sort()

        result = []

        for freq in freq_list[-k:]:
            for num in dic:
                if dic[num] == freq and num not in result:
                    result.append(num)
        return result