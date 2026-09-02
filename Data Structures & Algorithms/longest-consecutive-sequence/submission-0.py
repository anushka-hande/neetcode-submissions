class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        result = 0
        nums.sort()

        current = nums[0]
        sequence = 0
        i = 0
        while i < len(nums):
            if current != nums[i]:
                current = nums[i]
                sequence = 0
            while i < len(nums) and nums[i] == current:
                i += 1
            sequence += 1
            current += 1
            result = max(result, sequence)
        return result