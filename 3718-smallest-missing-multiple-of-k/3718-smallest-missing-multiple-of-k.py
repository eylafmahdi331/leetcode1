class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        numss = sorted(set(nums))
        multiples = list(range(k, 400, k))
        for i in multiples:
            if i not in numss:
                return i 
           
                    

        