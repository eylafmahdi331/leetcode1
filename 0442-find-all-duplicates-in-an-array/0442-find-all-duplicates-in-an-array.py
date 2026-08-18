class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        duplicates = {}

        for i in nums:
            duplicates[i] = duplicates.get(i, 0) + 1
        result = []

        for num, count in duplicates.items():
            if count > 1:
                result.append(num)
        return result
        