class Solution:
    def fib(self, n: int) -> int:
        def F(i):
            if i == 0:
                return 0
            elif i == 1:
                return 1
            else:
                return F(i - 1) + F(i - 2)
        return F(n)