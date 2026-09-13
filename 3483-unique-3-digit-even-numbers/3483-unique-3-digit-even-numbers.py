class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        even_count = set()

        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):

                    if i != j and j != k and i != k:

                        if digits[i] == 0:
                            continue

                        three_digit_num = str(digits[i]) + str(digits[j]) + str(digits[k])
                        num = int(three_digit_num)

                        if num % 2 == 0:
                            even_count.add(num)
        return (len(even_count))