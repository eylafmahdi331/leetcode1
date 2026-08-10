class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """

        if len(s) != len(goal):
            return False
        new = []
        for i in range(len(s)):
            new.append(s[i])
        counter = 0
        while counter < len(new):
            new.append(new[0])
            new.remove(new[0])
            new_str = ''.join(new)

            if new_str == goal:
                return True
                break
            else:
                if counter == len(new) - 1:
                    return False
                    break
  

 
            counter += 1
        