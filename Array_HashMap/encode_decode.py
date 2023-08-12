'''
Design an algorihm to encode a list of strings to a string. The encoded string is then 
sent over the network and is decoded back to the original list of strings.

Implement 'encode' and 'decode' 

Input: ["leet","code","love","you"]
Output: ["leet","code","love","you"]

Explanation:
One possible encode method is: "leet:;code:;love:;you"
'''
from typing import List
class Solution:

    def encode(self,strs):
        
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        

    def decode(self,str):
        
        res,i = [], 0

        #iterating till the length of whole string
        while i < len(str):
            j = i 
            while str[j] != "#": #iterating till we find '#' symbol
                j += 1
            
            length = int(str[i:j]) #recognizing the 
            res.append(str[j + i : j + 1 + length])
            i = j + 1 + length

        return res