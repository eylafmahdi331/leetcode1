class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        '''sorted_nums = sorted(nums)
        if len(nums) == 1:
            return False
            return
        else:
            for i in range (1, len(nums)):
         
                if sorted_nums[i] == sorted_nums[i-1]:
                    return True
                
        return False'''

        unique = set(nums)
    
        if len(nums) != len(unique):
            return True
        else: 
            return False
