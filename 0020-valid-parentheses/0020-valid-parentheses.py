class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        store = []

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        

        for i in s:
            if i in '({[':
                store.append(i)
    
            else:
                if not store or pairs[i] != store[-1]:
                    return False
                store.pop()


        return len(store) == 0


        