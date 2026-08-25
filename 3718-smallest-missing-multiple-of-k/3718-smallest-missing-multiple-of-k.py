class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
              
        for i in range(1, 1000):
            if i % k == 0 and i not in nums:
                return i 
           
                    

        