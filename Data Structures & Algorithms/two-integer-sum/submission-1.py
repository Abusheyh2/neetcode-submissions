class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            targets = target - num
            if targets in nums[i+1:]:
                return [i, nums[i+1:].index(targets) + (i+1)]
        return []