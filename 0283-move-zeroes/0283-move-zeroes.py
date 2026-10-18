class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        seek = 0
        pos = 0

        while seek < len(nums):
            if nums[seek] != 0:
                nums[pos], nums[seek] = nums[seek], nums[pos]
                pos += 1
            seek += 1
        return nums


        