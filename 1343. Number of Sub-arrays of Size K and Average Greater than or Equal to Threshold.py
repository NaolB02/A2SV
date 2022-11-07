class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, r = 0, k - 1
        curAverage = 0
        count = 0
        

        while r < len(arr):

            if l == 0:  curAverage = sum(arr[0:k]) / k
            else:   curAverage = ((curAverage * k) - arr[l - 1] + arr[r]) / k

            if curAverage >= threshold: count += 1
            l += 1
            r += 1
        
        return count
