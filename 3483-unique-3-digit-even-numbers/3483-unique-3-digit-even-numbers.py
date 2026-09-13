class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        import itertools

        even_count = [] # To store unique even three-digit numbers

# Generate all permutations of length 3 from the 'digits' list
        for p in itertools.permutations(digits, 3):
    # Form the three-digit number string
            num_str = "".join(map(str, p))

    # Convert to integer
            three_digit_num = int(num_str)

    # Check conditions:
    # 1. Numerically three-digit (i.e., between 100 and 999)
    # 2. Is even
    # 3. Not already in even_count list (to ensure uniqueness in the output)
            if three_digit_num % 2 == 0 and three_digit_num >= 100:
                if three_digit_num not in even_count:
                    even_count.append(three_digit_num)

        return(len(even_count))