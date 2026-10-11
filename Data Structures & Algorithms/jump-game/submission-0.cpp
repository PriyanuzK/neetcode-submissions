class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n =nums.size();
        int m = n - 1;
        int i;
        for(i =n-2;i>=0;i--){
            if (i + nums[i] >= m) {
                m = i;
            }
        }
        if(m==0){
            return true;
        }else{
            return false;
        }
        
    }
};
