class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.preSum = [nums[0]]
        for i in range(1, len(nums)):
            self.preSum.append(self.preSum[i - 1] + nums[i])  

    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right] - self.preSum[left] + self.nums[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
