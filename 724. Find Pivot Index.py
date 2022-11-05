class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        def findPreSum(arr):
            preSum = [0]
            for i in range(len(arr)):
                preSum.append(preSum[i] + arr[i])
            return preSum

        forwardPreSum = findPreSum(nums)
        nums.reverse()
        reversePreSum = findPreSum(nums)
        reversePreSum.reverse()

        for j in range(len(forwardPreSum) - 1):
            if forwardPreSum[j] == reversePreSum[j + 1]:
                return j
        
        return -1
