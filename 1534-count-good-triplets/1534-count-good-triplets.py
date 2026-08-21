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
            for j in range(i + 1,len(arr)):
                if (abs(arr[i] - arr[j]) > a):
                    continue
               
                for k in range(j + 1, len(arr)):
                        
                        if (abs(arr[j] - arr[k]) <= b) and (abs(arr[i] - arr[k]) <= c) :
                            total += 1
        return total

