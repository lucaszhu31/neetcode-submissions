class Solution:
    def trap(self, height: List[int]) -> int:
        l_max = 0
        r_max = 0
        l_max_arr = []
        r_max_arr = []
        water = 0

        for i in range(len(height)):
            j = -i-1
            l_max = max(height[i], l_max)
            r_max = max(height[j], r_max)
            l_max_arr.append(l_max)
            r_max_arr.append(r_max)
        
        r_max_arr = r_max_arr[::-1]

        for j in range(1,len(height) - 1):
            water_p_index = min(l_max_arr[j-1], r_max_arr[j+1]) - height[j]
            water_p_index = max(0,water_p_index)
            water += water_p_index
        return water
            


            
