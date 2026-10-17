class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        missing = []
        nums = set(nums)

        for i in range(1, n + 1):
            if i not in nums:
                missing.append(i)
        return missing


        