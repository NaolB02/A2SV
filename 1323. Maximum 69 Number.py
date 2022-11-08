class Solution:
    def maximum69Number (self, num: int) -> int:
        Snum = list(str(num))

        for i in range(len(Snum)):
            if Snum[i] == "6":
                Snum[i] = "9"
                break
        
        return int(''.join(Snum))
