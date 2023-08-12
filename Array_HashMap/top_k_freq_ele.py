'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.


'''
from typing import List
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