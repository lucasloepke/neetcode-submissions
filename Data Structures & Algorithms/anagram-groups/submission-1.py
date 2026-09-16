class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for i in strs:
            s = "".join(sorted(i))
            group[s].append(i)
        return list(group.values())
        