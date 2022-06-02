class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def pow(n):
            if n < 3 and n != 1:
                return False
            elif n == 1:
                return True
            n1 = n % 3
            n2 = n // 3
            if n1 == 0 and n2 == 1:
                return True
            else:
                return pow(n / 3)
        return pow(n)
