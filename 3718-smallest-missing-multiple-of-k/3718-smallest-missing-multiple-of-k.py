class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        multiple = [] 
        for i in range(1, 400):
            if i % k == 0:
                multiple.append(i)
        mul_set = sorted(set(multiple))     

        for i in mul_set:
            if i not in nums:
                return i

           
                    

        