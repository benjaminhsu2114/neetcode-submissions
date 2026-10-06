class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            cur = target - num
            
            if cur in seen:
                return[seen[cur], i]

            seen[num] = i
        return []
        # n = len(nums)

        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
