class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        str_digits= []
        for i in digits:
            str_digits.append(str(i))
        words = ''.join(str_digits)
        switch = int(words)
        plus = switch + 1
        plus = list(str(plus))
        for i in range(len(plus)):
            plus[i] = int(plus[i])
        return(plus)

        