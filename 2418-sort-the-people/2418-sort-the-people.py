class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        size = len(heights)

        for i in range(size):
            for j in range(i + 1, size):
                if heights[i] < heights[j]:
                    names[j], names[i] = names[i], names[j]
                    heights[j], heights[i] = heights[i], heights[j] 
                else:
                    continue
        return names



        