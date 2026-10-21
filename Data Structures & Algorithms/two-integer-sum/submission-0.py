class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_indices = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_indices:
                return [nums_indices[target - nums[i]], i]
            else:
                nums_indices[nums[i]] = i


        