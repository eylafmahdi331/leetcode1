class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seq = [nums[0]]
        for i in range (len(nums) - 1):
            
            
            j = nums[i+1] 
            if j- nums[i] == 1:

                seq.append(j)
                    

            else:
                break


        sum_seq = sum( seq)

        while sum_seq in nums:
                sum_seq += 1
           
        return sum_seq
        