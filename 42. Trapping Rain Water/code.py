class Solution:

    def trap(self, height: List[int]) -> int:
        #Find max from right, and from left
        max_left = [0 for x in height]
        max_right = [0 for x in height]
        max_left[0] = height[0]
        max_right[len(height)-1] = height[len(height)-1]
        l = 1
        r = len(height)-2
        while(l<len(height)):
            max_left[l] = max([max_left[l-1], height[l]])
            max_right[r] = max([max_right[r+1], height[r]])
            l+=1
            r-=1
        
        #Now find the sum by using the min of the two pillars forming a rain collection area
        sum1 = 0
        for i in range(len(max_left)):
            sum1+=max([0, min(max_left[i],max_right[i]) - height[i]])
        return sum1