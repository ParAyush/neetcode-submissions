class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for index, num in enumerate(nums):
            diff = target - num

            if diff in freq:

                return [freq[diff], index]
            freq[num] = index 