import math
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return int((n*2)/math.gcd(n,2) )