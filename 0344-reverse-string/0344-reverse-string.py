class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        right = len(s) - 1
        for left in range (len(s)):
            if right <= left:
                break

            s[left], s[right] = s[right], s[left]  
            right -= 1
    
        