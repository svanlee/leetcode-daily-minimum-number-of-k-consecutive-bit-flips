from typing import List

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip = 0
        is_flipped = [0] * n
        result = 0
        
        for i in range(n):
            if i >= k:
                flip ^= is_flipped[i - k]
            
            if flip % 2 == nums[i]:
                if i + k > n:
                    return -1
                flip ^= 1
                is_flipped[i] = 1
                result += 1
        
        return result