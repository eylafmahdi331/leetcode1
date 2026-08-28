class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        inter = []
        num1 = set(nums1)
        num2 = set(nums2)
        for i in num1:
            if i in num1 and i in num2:
                    inter.append(i)
        return (inter)

        

        