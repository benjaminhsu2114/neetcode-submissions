class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        h_map = {}
        l = 0
        

        for string in s1:
            if string not in h_map:
                h_map[string] = 1
            else:
                h_map[string] += 1

        for r in range(len(s2)):
            if s2[r] in h_map:
                h_map[s2[r]] -= 1

            w = r - l + 1
        
            if w > len(s1):
                if s2[l] in h_map:
                    h_map[s2[l]] += 1
                l += 1

            if all(value==0 for value in h_map.values()):
                return True

        return False

