class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        ans = []
        for i in range(len(nums)):
            temp = sorted_nums[:i] + sorted_nums[i+1:]
            j = 0
            k = len(temp) - 1

            while j < k:
                s = temp[j] + temp[k]
                target = -sorted_nums[i]
                if s == target:
                    triplet = []
                    triplet.append(sorted_nums[i])
                    triplet.append(temp[j])
                    triplet.append(temp[k])
                    triplet = sorted(triplet)
                    if triplet not in ans: 
                        ans.append(triplet)
                    j += 1
                    k -= 1
                elif s < target:
                    j += 1
                elif s > target:
                    k -= 1
        return ans

#did not trace properly first, then didnt take into account duplicates, 
#most importatbtly the break breaks the code 


                

        