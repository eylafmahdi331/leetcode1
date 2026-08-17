class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        arithmetic_series =(len_nums * (len_nums + 1)) // 2
        sum_nums = sum(nums)
        return arithmetic_series - sum_nums

        