class Solution(object):
    def findDifferentBinaryString(self, nums):
        n = len(nums)
        path = []

        def backtrack():
            if len(path) == n:
                result = "".join(path)

                if result not in nums:
                    return result

                return None

            for digit in ["0", "1"]:
                path.append(digit)

                result = backtrack()

                if result is not None:
                    return result

                path.pop()

            return None

        return backtrack()