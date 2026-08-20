class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        
        '''for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                if (((nums[i] == nums[j]) and (abs(i - (j)) <= k ))):
                    return True
          
   
        return False'''
        '''seen = {}

        for i, num in enumerate(nums):
            if num not in seen:
                seen[num] = []

            seen[num].append(i)
        for i in seen:
            if len(seen[i])> 1:


                for a in range(len(seen[i])):
                    for b in range(a + 1, len(seen[i])):

                        if abs(seen[i][a] - seen[i][b]) <= k:
                            return True

        return False'''
        seen = {}
        for i, num in enumerate(nums):
            if num in seen:
                if i - seen[num] <= k:
                    return True

            seen[num] = i
        return False
        