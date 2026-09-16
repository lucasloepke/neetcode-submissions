class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for x in strs:
            sortedx = ''.join(sorted(x))
            group[sortedx].append(x)
        return list(group.values())