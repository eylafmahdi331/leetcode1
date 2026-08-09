class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    

#arrsort = arr2)
#print (arrsort )
        max_prod = 0
        ordered = sorted(nums)

        for i in range (len(ordered)):
            if i == len(ordered) - 1:
                break
    
            if ((ordered[i] -1 ) * (ordered[i+1] -1)) >= max_prod :
                max_prod = ((ordered[i] -1 ) * (ordered[i+1] -1))
        return(max_prod)

        


        