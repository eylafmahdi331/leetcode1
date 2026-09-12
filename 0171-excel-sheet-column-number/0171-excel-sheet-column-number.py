class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        import string
        letters = list(string.ascii_uppercase)
        
        total = 0
        power = len(columnTitle) - 1
        for i in columnTitle:
            value = letters.index(i) + 1
            total += value * (26 ** power) 
            power -= 1
        return(total)
            
        