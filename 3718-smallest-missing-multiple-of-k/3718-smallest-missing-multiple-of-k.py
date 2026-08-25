class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter

        d = Counter(nums)       
        for i in range(1, 1000):
            if i % k == 0 and i not in d:
                return i 
           
                    

        