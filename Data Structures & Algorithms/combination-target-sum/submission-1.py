class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        path=[]
        def dfs(i,path,remaining):
            if remaining==0:
                res.append(path.copy())
                return
            for j in range(i,len(nums)):
                if nums[j]>remaining:
                    continue
                path.append(nums[j])
                dfs(j,path,remaining-nums[j])  
                path.pop()
        dfs(0,path,target)
        return res    
