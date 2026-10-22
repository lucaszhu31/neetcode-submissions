class Solution:
    def trap(self, height: List[int]) -> int:
        l_max_array, r_max_array = [], [] 
        l_max, r_max = 0, 0

        #Initialize the left max height and right max height at position i 
        for l in range(len(height)):
            r = -l-1
            l_max = height[l] if height[l] > l_max else l_max
            r_max = height[r] if height[r] > r_max else r_max
            l_max_array.append(l_max)
            r_max_array.append(r_max)
        
        r_max_array = r_max_array[::-1]

        total_water = 0
        i = 1
        j = len(height) - 2
        for i in range(1,len(height)-1):
            water = min(l_max_array[i], r_max_array[i]) - height[i]
            water = 0 if water < 0 else water 
            total_water += water 
        
        return total_water


        