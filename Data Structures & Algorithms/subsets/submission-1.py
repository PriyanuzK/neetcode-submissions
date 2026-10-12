
class Solution:
    def subsets(self, nums):
        result = []
        path = []

        def dfs(i):
            if i == len(nums):
                result.append(path.copy())
                return

         
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

            
            dfs(i + 1)

        dfs(0)
        return result

