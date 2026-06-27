class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}

        for dup in nums:
            if dup in freq:
                freq[dup] +=1
                return True
            else:
                freq[dup] = 1

        return False


                