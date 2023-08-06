#space complexity = O(1)
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
