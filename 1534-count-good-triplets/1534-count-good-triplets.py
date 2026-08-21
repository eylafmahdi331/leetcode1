class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        total = []
       
        for i in range((len(arr))):
            for j in range(1,((len(arr)))):
                for k in range(2, len(arr)):
                    if 0 <= i < j < k < len(arr):
                        if (abs(arr[i] - arr[j]) <= a) and (abs(arr[j] - arr[k]) <= b) and (abs(arr[i] - arr[k]) <= c):
                            total.append((arr[i], arr[j], arr[k]))
        return len(total)

