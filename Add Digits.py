class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            i =  (1 +(num -1) % 9)
            return i
        else: 
            return num
           




        
