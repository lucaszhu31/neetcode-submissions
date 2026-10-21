class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Brute force o(n^2)
        # output = []
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if j != i:
        #             product *= nums[j]
        #     output.append(product)
        # return output 
        left_output = []
        right_output = []
        output = []

        left_side_prod = 1
        right_side_prod = 1
        for i in range(len(nums)):
            if i == 0:
                left_output.append(left_side_prod)
            else: 
                left_side_prod *= nums[i-1]
                left_output.append(left_side_prod)


        
        for j in range(len(nums)-1,-1, -1):
            if j == len(nums) - 1:
                right_output.append(right_side_prod)
            else:
                right_side_prod *= nums[j+1]
                right_output.append(right_side_prod)
                
        for l, r in zip(left_output, reversed(right_output)):
            output.append(l * r)

        return output 

        
                
            
            

            
        