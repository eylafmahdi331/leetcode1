class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        output = []
        num1 = sorted(nums1)
        num2 = sorted(nums2)
        i,j = 0, 0 
        while i<len(num1) and j < len(num2):
            if num1[i] > num2[j]:
                j +=1 
            elif num1[i] < num2[j]:
                i +=1
            else:
                output.append(num1[i])
                i +=1
                j +=1
        return output






        '''output = []
        
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                output.append(nums1[i])
        return output'''
