class Solution(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """
        count = 0
        for i in range(limit + 1):
            for j in range (limit +1):
                for k in range (limit +1):
                    if sum([i, j, k]) == n:
    
       
                        count +=1
        return count


                


 