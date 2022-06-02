class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def pow(n):
            if n < 4 and n != 1:
                return False
            elif n == 1:
                return True
            n1 = n % 4
            n2 = n // 4
            if n1 == 0 and n2 == 1:
                return True
            else:
                return pow(n / 4)
        return pow(n)