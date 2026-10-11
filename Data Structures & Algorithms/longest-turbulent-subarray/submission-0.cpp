class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {
        int n =arr.size();
        int curr=1, maxlen=1;
        for(int i=1;i<n;i++){
            if(i>=2&&((arr[i]>arr[i-1] && arr[i-1]<arr[i-2])|| (arr[i]<arr[i-1]&&arr[i-1] > arr[i-2]))){
                curr++;
            }else if(arr[i]!=arr[i-1]){
                curr =2;
            }else{
                curr=1;
            }
            maxlen=max(maxlen,curr);
        }
 return maxlen;


    }
        
        
    
};