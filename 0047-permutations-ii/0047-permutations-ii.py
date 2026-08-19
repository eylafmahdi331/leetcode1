class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path = []
        final = []
        used = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                final.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                    

                used[i] = True
                path.append(nums[i])

                backtrack()

                path.pop()
                used[i] = False

        backtrack()

        return  [list(x) for x in set(tuple(x) for x in final)]





















 