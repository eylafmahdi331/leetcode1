class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set()
        dup = []

        for i in nums:
            if i in seen:
                dup.append(i)
            else:
                seen.add(i)
        return dup
            



        
        