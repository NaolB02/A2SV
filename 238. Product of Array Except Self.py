class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forProduct = [nums[0]]
        backProduct = [nums[len(nums) - 1]]
        out = [None] * len(nums)
        
        for i in range(1, len(nums)):
            forProduct.append(forProduct[i - 1] * nums[i])
        
        i = 1
        for j in range(len(nums) - 2, -1, -1):
            backProduct.append(backProduct[i - 1] * nums[j])
            i += 1
        backProduct.reverse()

        for k in range(len(forProduct)):
            if k == 0:
                out[k] = backProduct[1]
            elif k == len(nums) - 1:
                out[k] = forProduct[len(nums) - 2]
            else:
                out[k] = forProduct[k - 1] * backProduct[k + 1]

        return out        
            
