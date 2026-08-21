class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        total = 0
       
        for i in range(len(arr)):
            for j in range(1,len(arr)):
                if (abs(arr[i] - arr[j]) > a):
                    continue
               
                for k in range(2, len(arr)):
                        
                        if (abs(arr[j] - arr[k]) <= b) and (abs(arr[i] - arr[k]) <= c) and i < j < k < len(arr) :
                            total += 1
        return total

