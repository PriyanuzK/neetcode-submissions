class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >=goal: # nums[i] will be the jump length if it id greater then it means we can reach the goal
                goal=i
        return True if goal ==0 else False        
