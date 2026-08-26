class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        d = Counter(nums)
        for key, value in d.items():
            if value ==1:
                return key
          