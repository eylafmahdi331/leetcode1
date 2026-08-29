class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dicts = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key not in dicts:
                dicts[key] = []
            dicts[key].append(word)

        return list(dicts.values())

        