class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set()
        dup = []

        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                dup.append(i)
        return dup
            



        
        