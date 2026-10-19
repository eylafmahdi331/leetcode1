class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people = sorted(people)

        i = 0
        j = len(people) - 1
        count = 0

        while i <= j:
            if i < j and people[i] + people[j] > limit:
                count += 1
                j -= 1
            else:
                count += 1
                j -= 1
                i += 1

        return count




        