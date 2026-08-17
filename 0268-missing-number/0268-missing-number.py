class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = sorted(nums)
        for i in range(len(set_nums) + 1):
            if i not in nums:
                return i