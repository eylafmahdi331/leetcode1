class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        new = ""
        for char in range(len(s) - 1, -1, -1):
            if s[char] == " ":
                continue
            else:
                new += s[char]
                if s[char - 1] == ' ':
                    break
        return(len(new))