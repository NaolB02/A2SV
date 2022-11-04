class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        tempset = set()
        l, r = 0, 0
        
        while r < len(s):

            if s[r] not in tempset:
                tempset.add(s[r])
                
                if len(tempset) > maxLength:
                    maxLength = len(tempset)
                
                r += 1
                
            else:
                tempset.remove(s[l])
                l += 1
            
    
        return maxLength
