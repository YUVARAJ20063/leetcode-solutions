class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        first=0
        last=(len(x)-1)
        while first < last:
            if x[first] != x[last]:
                return False
            first += 1
            last -= 1
        return True