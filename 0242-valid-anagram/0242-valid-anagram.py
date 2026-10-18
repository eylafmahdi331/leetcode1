class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = sorted(list(s))
        t = sorted(list(t))

        if s == t:
            return True
        else:
            return False
        