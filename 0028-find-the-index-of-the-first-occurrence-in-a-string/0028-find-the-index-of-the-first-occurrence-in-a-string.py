class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        start = 0
        i, j = start,0
        
        if (len (needle) > len(haystack)) or len(needle) == 0:
            return -1
        

        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return  start
            else:
                start += 1
                i = start
                j = 0
                
        return -1
            
                

        