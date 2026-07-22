class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            width = right - left
            min_height = min(height[left], height[right])
            current_water = width * min_height
            max_water = max(max_water, current_water)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water

# Test it
sol = Solution()

# Test case 1
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49

# Test case 2
print(sol.maxArea([1, 1]))  # 1

# Test case 3
print(sol.maxArea([4, 3, 2, 1, 4]))  # 16