class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        idx_map = {}
        for i,n in enumerate(nums):
            check= target- nums[i]
            if check in idx_map:
                return [idx_map[check],i]
            idx_map[n]=i

        