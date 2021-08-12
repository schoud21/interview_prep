class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_qnt=0
        while left<right:
            if height[left]>height[right]:
                max_qnt=max(max_qnt, height[right]*(right-left))
                right-=1
            else:
                max_qnt=max(max_qnt, height[left]*abs(right-left))
                left+=1
        return max_qnt

