class Solution:

    def encode(self, strs: List[str]) -> str:
        combined = ""
        for i in strs:
            combined += (str(len(i)) + "." + i)
        return combined

    def decode(self, s: str) -> List[str]:
        final = []
        while s != "":
            dot_index = s.find('.')
            length_str = int(s[:dot_index])
            final.append(s[dot_index+1:length_str+dot_index+1])
            s = s[dot_index+length_str+1:]
        return final