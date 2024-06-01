class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        l=[]
        for i in words:
            if i==i[::-1]:
                l.append(i)
        if l==[]:
            return ""
        else:
            return l[0]