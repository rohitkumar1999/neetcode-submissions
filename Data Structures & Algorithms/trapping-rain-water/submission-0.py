class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left,right = [0]*n,[0]*n 
        left[0] = 0
        right[n-1] = 0
        for i in range(1,n):
            left[i]=max(left[i-1],height[i-1])
            right[n-i-1]=max(right[n-i],height[n-i])
        
        water=0
        for i in range(n):
            if height[i] < min(left[i],right[i]):
                water+= min(left[i],right[i])-height[i]
        
        return water
        

        