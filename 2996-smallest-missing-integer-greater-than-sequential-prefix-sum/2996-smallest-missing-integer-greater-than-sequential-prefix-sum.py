class Solution(object):
    def missingInteger(self, nums):
        seq = [nums[0]]

        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i] + 1:
                seq.append(nums[i + 1])
            else:
                break

        sum_seq = sum(seq)

        while sum_seq in nums:
            sum_seq += 1

        return sum_seq