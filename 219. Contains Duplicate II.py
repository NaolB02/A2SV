def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        numsDict = {}
        

        while i < len(nums):

            if nums[i] in numsDict and abs(numsDict[nums[i]] - i) <= k:
                    return True
        
            numsDict[nums[i]] = i
            i += 1

        return False
