from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort to handle duplicates
        
        def backtrack(start: int, path: List[int]):
            res.append(path[:])  
            
            for i in range(start, len(nums)):
                # Skip duplicates on the same tree level
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0, [])
        return res
