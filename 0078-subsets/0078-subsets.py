class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        #helper for subsets 
        def backtrack(start,path):
            res.append(path[:])
            for i in range(start,len(nums)):
                path.append(nums[i]) # choose
                backtrack(i+1,path) # explore
                path.pop() # undo
        backtrack(0,[])
        return res
        