class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        i = len(nums)
        h = 0
        mins = []
        while h < i:
            numss = []
            for j in range(h, i ):
                numss.append(nums[j])
  #print(k)
            mins.append(min(numss))



            h += 1
        i = 1
        maxs = []

        while i < (len(nums) + 1):
            numsss = []
            for j in range(i ):
                numsss.append(nums[j])
  #print(k)
            maxs.append(max(numsss))


            i += 1
        for i in range(len(nums)):
            score = maxs[i] - mins[i]
            if score <= k:
                return i
        return (-1) 

        
        