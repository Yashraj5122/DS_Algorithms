#space complexity = O(1)
'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
 
Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

       #using simple sort and compare 
        s = [x for x in s]
        t = [x for x in t]

        s.sort()
        t.sort()

        if s == t:
            return True
        else:
            return False
        

# #using hashmap
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         countS , countT = {} , {}

#         for i in range(len(s)):
#             countS[s[i]] = 1 + countS.get(s[i],0) 
#             countT[t[i]] = 1 + countT.get(t[i],0)
        
#         return countS == countT
