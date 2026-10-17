class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        counter = {}
        missing = []
        

        for i in nums:
            counter[i] = counter.get(i, 0) + 1
        for i in range(1, n + 1):
            if i not in counter:
                missing.append(i)
        return missing


        