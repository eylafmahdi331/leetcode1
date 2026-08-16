class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        high = len(nums) - 1
        low = 0

        if target not in nums:
            nums.append(target)
            nums.sort()
            return nums.index(target)

        while low <= high:
            middle  = (low + high) // 2
            if nums[middle] == target:
                return middle
                break
            elif nums[middle] < target:
                low = middle + 1
            else:
                high = middle - 1
        