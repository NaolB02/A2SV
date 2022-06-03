class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count_list = []
        for i in nums:
            count = 0
            for j in nums:
                if j < i:
                    count += 1
            count_list.append(count)
        return count_list  