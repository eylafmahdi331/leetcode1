class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or not all(word.isalnum() for word in strs):
            return ""
        if len(strs) <= 1:
                return strs[0]
        prefix = ""
        current_str = strs[0]

        for j in range(len(current_str)):
            pair = current_str[j:j+1]

            if all(len(word) > j and word[j] == pair for word in strs):
                prefix += pair
            else:
                break

        return prefix