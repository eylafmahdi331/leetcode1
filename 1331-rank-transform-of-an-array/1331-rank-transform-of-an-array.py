class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arrSorted = sorted(arr)
        rank = 1
        dic = {}

        for i, j in enumerate(arrSorted):
            if j not in dic:
                dic[j] = rank
                rank += 1

        ans = []

        for i in arr:
            ans.append(dic[i])

        return ans

