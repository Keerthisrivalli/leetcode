class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = []
        count = 0
        for i in range(len(s)):
            l.append(s[i])
            if l.count('R') == l.count('L'):
                count += 1
                l.clear()
        return count
        